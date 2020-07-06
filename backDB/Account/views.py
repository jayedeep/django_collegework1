from django.shortcuts import render
from rest_framework import generics, filters
from .models import College, Students, Professors,CustomUser
from .serializers import Customeserializer,Collegeserializer, Professorserializer, Studentserializer
# Create your views here.
from .permissions import IsProfessor,IsCollege,IsStudent
from rest_framework.permissions import AllowAny
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class Customeusers(generics.CreateAPIView):
    serializer_class = Customeserializer
    permission_classes = (AllowAny)
#
# class Customeusers(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = Customeserializer
#     permission_classes = (IsCollege)
#
# class Customeusers(generics.UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = Customeserializer
#     permission_classes = (IsCollege)
#
# class Customeusers(generics.DestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = Customeserializer
#     permission_classes = (IsCollege)
#-----------------------------------------------------
class CollegeUsers(generics.CreateAPIView):
    serializer_class = Collegeserializer
    permission_classes = (IsCollege)

class CollegeUsers(generics.ListAPIView):
    queryset = College.objects.all()#changesssssss
    serializer_class = Collegeserializer
    permission_classes = (IsCollege)

class CollegeUsers(generics.UpdateAPIView):
    queryset = College.objects.all()#changesssssss
    serializer_class = Collegeserializer
    permission_classes = (IsCollege)

class CollegeUsers(generics.DestroyAPIView):
    queryset = College.objects.all()#changesssssss
    serializer_class = Collegeserializer
    permission_classes = (IsCollege)

class CollegeUsers(generics.RetrieveAPIView):
    queryset = College.objects.all()#changesssssss
    serializer_class = Collegeserializer
    permission_classes = (IsCollege)

#-------------------------------------------------
class ProfessorUsers(generics.CreateAPIView):
    serializer_class = Professorserializer
    permission_classes = (IsProfessor|IsCollege)

class ProfessorUsers(generics.ListAPIView):
    queryset = Professors.objects.all()#changesssssss
    serializer_class = Professorserializer
    permission_classes = (IsProfessor|IsCollege)

class ProfessorUsers(generics.UpdateAPIView):
    queryset = Professors.objects.all()#changesssssss2
    serializer_class = Professorserializer
    permission_classes = (IsProfessor|IsCollege)

class ProfessorUsers(generics.DestroyAPIView):
    queryset = Professors.objects.all()#changesssssss
    serializer_class = Professorserializer
    permission_classes = (IsCollege)

class ProfessorUsers(generics.RetrieveAPIView):
    queryset = Professors.objects.all()#changesssssss
    serializer_class = Professorserializer
    permission_classes = (IsProfessor|IsCollege)

#-----------------------------------------------
class ProfessorUsers(generics.CreateAPIView):
    serializer_class = Professorserializer
    permission_classes = (IsProfessor)

class ProfessorUsers(generics.ListAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = (IsProfessor)

class ProfessorUsers(generics.UpdateAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = (IsProfessor)

class ProfessorUsers(generics.DestroyAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = (IsProfessor)

class ProfessorUsers(generics.RetrieveAPIView):
    queryset = Professors.objects.all()
    serializer_class = Professorserializer
    permission_classes = (IsProfessor)




# class Customeusers(generics.RetrieveAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = Customeserializer
#     permission_classes = (IsCollege)
#
#
# class ListCustomeUsers(generics.ListCreateAPIView):
#     # search_fields = ['name']
#     # filter_backends = (filters.SearchFilter,)
#     queryset = CustomUser.objects.all()
#     serializer_class = Customeserializer
#
# class DetailCustomeUsers(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = Customeserializer
#
#
# class ListColleges(generics.ListCreateAPIView):
#     # search_fields = ['name']
#     # filter_backends = (filters.SearchFilter,)
#     queryset = College.objects.all()
#     serializer_class = Collegeserializer
#
# class DetailColleges(generics.RetrieveUpdateDestroyAPIView):
#     queryset = College.objects.all()
#     serializer_class = Collegeserializer
#
#
#
# class ListStudents(generics.ListCreateAPIView):
#     search_fields = ['name', '=semester', '=enrollment', 'department','college__name']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Students.objects.all()
#     serializer_class = Studentserializer
#
# class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Students.objects.all()
#     serializer_class = Studentserializer
#
#
#
# class ListProfessors(generics.ListCreateAPIView):
#     search_fields = ['name','department', '=role','college__name']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Professors.objects.all()
#     serializer_class = Professorserializer
#
# class DetailProfessors(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Professors.objects.all()
#     serializer_class = Professorserializer