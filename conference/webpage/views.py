from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Landingpage, About, Partner, Schedule, Photos, Address, Highlightpoints, Speakers, Faq, Developedby, Ticket, Register
from .email_api.send_mail import send

def home(request):
    landing_details = Landingpage.objects.order_by('-created_date')
    about = About.objects.order_by('-created_date')
    hightlighpoints = Highlightpoints.objects.order_by('-created_date')
    partner = Partner.objects.order_by('-created_date')
    schedule = Schedule.objects.order_by('-created_date')
    photos = Photos.objects.order_by('-created_date')
    address = Address.objects.order_by('-created_date')
    speakers = Speakers.objects.order_by('-created_date')
    speaker_count = Speakers.objects.order_by('-created_date').count()
    faq = Faq.objects.order_by('-created_date')
    developed_by = Developedby.objects.order_by('-created_date')
    ticket = Ticket.objects.order_by('-created_date')

    register_count = Register.objects.filter(status="Registered").count()
    confirmed_count = Register.objects.filter(status="Confirmed").count()
    hold_count = Register.objects.filter(status="Hold").count()
    ticket_no = Ticket.objects.values("ticket_no")[0]['ticket_no']
    extras_no = Ticket.objects.values("extras_no")[0]['extras_no']
    ticket_obj = Ticket.objects.order_by('-created_date')[0]

    if (register_count + confirmed_count + hold_count) == (ticket_no + extras_no):
        ticket_obj.status = "Closed"
        ticket_obj.save()
    else:
        ticket_obj.status = "Open"
        ticket_obj.save()

    
    while (hold_count > 0) and (0 < (register_count + confirmed_count) < ticket_no) : # 0 is gven to avoid error when no users have registered
        hold_obj = Register.objects.filter(status="Hold")[0]
        hold_obj.status = "Registered"
        hold_obj.save()
        register_count = Register.objects.filter(status="Registered").count()

    data = {
        'landing_details' : landing_details,
        'about' : about,
        'hightlighpoints' : hightlighpoints,
        'partner' : partner,
        'schedule' : schedule,
        'photos' : photos,
        'address' : address,
        'speakers' : speakers,
        'speaker_count' : str(speaker_count),
        'faq' : faq,
        'developed_by' : developed_by,
        'ticket' : ticket,
    }
    return render(request, 'webpage/index.html', data)


def register(request):
    ticket = Ticket.objects.order_by('-created_date')[0]

    register_count = Register.objects.filter(status="Registered").count()
    confirmed_count = Register.objects.filter(status="Confirmed").count()
    ticket_no = Ticket.objects.values("ticket_no")[0]['ticket_no']
    extras_no = Ticket.objects.values("extras_no")[0]['extras_no']

    if request.method == 'POST' and ticket.status=='Open':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        program = request.POST['program']
        phone = request.POST['phone']
        zip = request.POST['zip']
        email = request.POST['email']
        address = request.POST['address']

        try:
            match = Register.objects.get(email=email)
            messages.warning(request, 'Email already exists')
            raise ValidationError(('Email already exists'), code='invalid')

        except Register.DoesNotExist:
            # Unable to find a user, this is fine
            if (register_count + confirmed_count ) < ticket_no:
                status = "Registered"
            elif (register_count + confirmed_count ) < ticket_no + extras_no:
                status = "Hold"

            register = Register(first_name=first_name, last_name=last_name, city=city, program=program, status=status, phone=phone, email=email, address=address, zip=zip)
            register.save()
            messages.success(request, 'Thanks for reaching out!')
            send(email, first_name, program, status = status)
        return redirect('home')