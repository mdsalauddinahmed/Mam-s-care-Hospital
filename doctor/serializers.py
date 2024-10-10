from rest_framework import serializers

from .import models


class Specializationserializer(serializers.ModelSerializer):
 
    class Meta:
        model= models.Specialization
        fields= '__all__'
class Designationserializer(serializers.ModelSerializer):
   
    class Meta:
        model= models.Designation
        fields= '__all__'
class AvailaleTimeserializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model= models.AvailaleTime
        fields= '__all__'
class Doctorserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    avaiiable_time = serializers.StringRelatedField(many=True)
    class Meta:
        model= models.Doctor
        fields= '__all__'
class Reviewserializer(serializers.ModelSerializer):
   
    class Meta:
        model= models.Review
        fields= '__all__'