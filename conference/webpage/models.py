from email.policy import default
from django.db import models
from datetime import date, datetime
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, post_init
from .email_api.send_mail import send

STATUS = [
    ('Registered', 'Registered'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
    ('Hold', 'Hold'),
]

TICKET_STATUS = [
    ('Open', 'Open'),
    ('Closed', 'Closed'),
]

PROGRAM = [
    ('Workshop', 'Workshop'),
    ('Tech Talk' , 'Tech Talk'),
    ('Conference', 'Conference'),
]


# Create your models here.
class Landingpage(models.Model):
    title = models.CharField(max_length=255)
    conference_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/landing/logo/')
    conference_date = models.DateTimeField(default=datetime.now, blank=True)
    conference_hallname = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class About(models.Model):
    photo = models.ImageField(upload_to='media/about-us/%Y')
    description = RichTextField()
    goal_description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Highlightpoints(models.Model):
    highlight_points = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Partner(models.Model):
    logo = models.ImageField(upload_to='media/partner/%Y/%m')
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Schedule(models.Model):
    title = models.CharField(max_length=255)
    speaker_name = models.CharField(max_length=255)
    start_time = models.DateTimeField(default=datetime.now, blank=True)
    end_time = models.DateTimeField(default=datetime.now, blank=True)
    speaker_designation = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Photos(models.Model):
    image = models.ImageField(upload_to='media/photos/%Y/%m')
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Address(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    address = RichTextField()
    email = models.EmailField()
    google_map_embed_location = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Speakers(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/speakers/%Y/%m')
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    fb_link = models.URLField()
    email = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Faq(models.Model):
    headline = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Developedby(models.Model):
    company_name = models.CharField(max_length=255)
    company_website =  models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    fb_link = models.URLField()
    email = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Ticket(models.Model):
    ticket_no = models.IntegerField()
    extras_no = models.IntegerField()
    status = models.CharField(max_length=255, default="Open", choices=TICKET_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

class Register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    program = models.CharField(max_length=255, choices=PROGRAM)
    phone = PhoneNumberField()
    email = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    address = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default="Registered", choices=STATUS)
    previous_status = None

    @staticmethod
    def post_save(sender, instance, created, **kwargs):
        print("instance.previous_status :", instance.previous_status)
        print("instance.status :", instance.status)
        if instance.previous_status != instance.status:
            print("True")
            send(instance.email, instance.first_name, instance.program, status = instance.status)
    @staticmethod
    def remember_status(sender, instance, **kwargs):
        instance.previous_status = instance.status
        print("Previous Status : ", instance.previous_status)

post_save.connect(Register.post_save, sender=Register)
post_init.connect(Register.remember_status, sender=Register)