# Generated by Django 4.0.4 on 2022-08-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('department', '0003_remove_classroom_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(blank=True, to='student.student'),
        ),
    ]
