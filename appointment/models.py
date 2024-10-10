from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailaleTime

# Create your models here.

APPOINTMENT_STATUS=[
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running')
]
APPOINTMENT_TYPES=[
    ('online','online'),
    ('offline','offline')
  
]
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    symtoms= models.TextField()
    appointemt_status=models.CharField(choices=APPOINTMENT_STATUS,max_length=100,default='Pending')
    appointment_types = models.CharField(choices=APPOINTMENT_TYPES,max_length=100)
    time=models.ForeignKey(AvailaleTime,on_delete=models.CASCADE)
    cancel = models.BooleanField()

    
    def __str__(self) -> str:
        return f"Doctor: {self.doctor.user.first_name}; Patient: {self.patient.user.first_name}"
    

     
