# Generated by Django 4.0.4 on 2022-08-04 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('student', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='hod_faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.contactdetails'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.branch'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.contactdetails'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(to='student.student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.subject'),
        ),
        migrations.AddField(
            model_name='branchsubject',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.branch'),
        ),
        migrations.AddField(
            model_name='branchsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.subject'),
        ),
        migrations.AddField(
            model_name='branch',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department'),
        ),
        migrations.AddField(
            model_name='assingment',
            name='classroom_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.classroom'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
