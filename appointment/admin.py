from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['patient_name','doctor_name','appointemt_status','appointment_types','symtoms','time','cancel']
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appointemt_status == "Running" and obj.appointment_types == "online":
            email_subject="Your online appointment is Running"
            email_body =render_to_string ('admin_mail.html',{'user':obj.patient.user,'doctor':obj.doctor.user})
            email =EmailMultiAlternatives(email_subject,'', to=[obj.patient.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
    
admin.site.register(Appointment,AppointmentAdmin)   