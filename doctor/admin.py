from django.contrib import admin

 
from .models import AvailaleTime,Specialization,Designation,Doctor ,Review

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

admin.site.register(AvailaleTime)

admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(Doctor)
admin.site.register(Review)