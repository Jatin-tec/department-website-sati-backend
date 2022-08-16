from django.db import models
from department.models import *

class ComputerScience(models.Model):
    STATUS = (
        ("PRESENT", "Present"),
        ("ABSENT", "Absent"),
        ("LEAVE", "Leave"),
    )
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    teacher = models.ForeignKey('faculty.ContactDetails', on_delete=models.CASCADE)
    class_room = models.ForeignKey('department.ClassRoom', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, verbose_name="status")
    date = models.DateField(default = timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['student', 'teacher', 'class_room', 'date']
        ordering = ['date']

class ArtificalIntelligenceAndDataScience(models.Model):
    STATUS = (
        ("PRESENT", "Present"),
        ("ABSENT", "Absent"),
        ("LEAVE", "Leave"),
    )
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    teacher = models.ForeignKey('faculty.ContactDetails', on_delete=models.CASCADE)
    class_room = models.ForeignKey('department.ClassRoom', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, verbose_name="status")
    date = models.DateField(default = timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['student', 'teacher', 'class_room', 'date']
        ordering = ['date']