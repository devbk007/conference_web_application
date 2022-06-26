from django.contrib import admin
from . import models
from django.utils.html import format_html

class LandingpageAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html('<img src="{}" width="40" height="40"/>'.format(object.logo.url))
    
    list_display = ('conference_name','title', 'pic', 'edited_date')
    list_display_links = ('conference_name',)

class HightlightpointsAdmin(admin.ModelAdmin):
    list_display = ('highlight_points', 'edited_date')
    list_display_links = ('highlight_points',)
    ordering = ['-edited_date']

class PartnerAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html('<img src="{}" width="40" height="40"/>'.format(object.logo.url))
    
    list_display = ('pic', 'edited_date')
    list_display_links = ('pic',)
    ordering = ['-edited_date']

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'speaker_name', 'title')
    list_display_links = ('title',)
    ordering = ['-edited_date']

class PhotoAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html('<img src="{}" width="40" height="40"/>'.format(object.image.url))
    
    list_display = ('pic', 'edited_date')
    list_display_links = ('pic',)
    ordering = ['-edited_date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'edited_date')
    list_display_links = ('name',)

class SpeakersAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'edited_date')
    list_display_links = ('name',)

class FaqAdmin(admin.ModelAdmin):
    list_display = ('headline', 'edited_date')
    list_display_links = ('headline',)

class DevelopedbyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'edited_date')
    list_display_links = ('company_name',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_no', 'extras_no', 'status')
    list_display_links = ('ticket_no',)

class RegisterAdmin(admin.ModelAdmin):
    
    def name(self, object):
        return ("%s %s" % (object.first_name, object.last_name))
    
    list_display = ('name', 'email', 'status', 'phone')
    list_display_links = ('name',)

# Register your models here.
admin.site.register(models.Landingpage, LandingpageAdmin)
admin.site.register(models.About)
admin.site.register(models.Highlightpoints, HightlightpointsAdmin)
admin.site.register(models.Partner, PartnerAdmin)
admin.site.register(models.Schedule, ScheduleAdmin)
admin.site.register(models.Photos, PhotoAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Speakers, SpeakersAdmin)
admin.site.register(models.Faq, FaqAdmin)
admin.site.register(models.Developedby, DevelopedbyAdmin)
admin.site.register(models.Ticket, TicketAdmin)
admin.site.register(models.Register, RegisterAdmin)