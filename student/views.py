from django.shortcuts import render
from rest_framework import generics, permissions, mixins, authentication
from student.models import Student
from student.serializers import *
from faculty.models import *
from faculty.serializers import *
from department_website_sati.authentication import TokenAuthentication
from department_website_sati.mixins import StaffEditorPermissionMixin

class StudentDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView
    ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    lookup_field = 'scholar_no'

student_detail_view = StudentDetailAPIView.as_view()

class StudentListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        print(serializer)
        serializer.save()

student_list_create_view = StudentListCreateAPIView.as_view()

class StudentUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView
    ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

student_update_view = StudentUpdateAPIView.as_view()

class StudentDeleteAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView
    ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'scholar_no'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

student_delete_view = StudentDeleteAPIView.as_view()
