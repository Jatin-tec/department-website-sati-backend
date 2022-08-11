# Generated by Django 4.0.4 on 2022-08-04 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attendance', '0001_initial'),
        ('student', '0001_initial'),
        ('department', '0001_initial'),
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerscience',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.classroom'),
        ),
        migrations.AddField(
            model_name='computerscience',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='computerscience',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.contactdetails'),
        ),
        migrations.AddField(
            model_name='artificalintelligenceanddatascience',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.classroom'),
        ),
        migrations.AddField(
            model_name='artificalintelligenceanddatascience',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AddField(
            model_name='artificalintelligenceanddatascience',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.contactdetails'),
        ),
        migrations.AlterUniqueTogether(
            name='computerscience',
            unique_together={('student', 'teacher', 'class_room', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='artificalintelligenceanddatascience',
            unique_together={('student', 'teacher', 'class_room', 'date')},
        ),
    ]
