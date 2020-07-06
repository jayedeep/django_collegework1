from rest_framework import serializers
from .models import College, Students, Professors,CustomUser


class Customeserializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ['password','email','user_type']

class Collegeserializer(serializers.ModelSerializer):
    class Meta:
        model= College
        fields = '__all__'

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model= Students
        fields = '__all__'
    
class Professorserializer(serializers.ModelSerializer):
    class Meta:
        model= Professors
        fields = '__all__'