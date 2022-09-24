from django.db import models
from department.models import *
from django.conf import settings
from django.utils import timezone 

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    scholar_no = models.IntegerField(unique=True, blank=True, null=True)
    enrollment_no = models.CharField(max_length=20, unique=True, blank=True, null=True)
    branch = models.ForeignKey('department.Branch', on_delete=models.CASCADE, blank=True, null=True) 


    