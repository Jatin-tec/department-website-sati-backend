# Generated by Django 4.0.4 on 2022-08-04 03:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('role', models.CharField(blank=True, max_length=20, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assingment',
            fields=[
                ('title', models.CharField(max_length=256, verbose_name='Name of quiz')),
                ('question', models.CharField(max_length=1000, verbose_name='Question')),
                ('assingment_file', models.FileField(blank=True, null=True, upload_to='assingments/file', verbose_name='Assingment file')),
                ('image', models.ImageField(blank=True, null=True, upload_to='assingments/image', verbose_name='Assingment image')),
                ('maximum_marks', models.IntegerField(verbose_name='Total marks of assingment')),
                ('primary_key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Date added')),
                ('due_date', models.DateField(blank=True, default='', null=True, verbose_name='Due added')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('branch_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BranchSubject',
            fields=[
                ('uid', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('classroom_code', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('class_name', models.CharField(blank=True, max_length=50, null=True)),
                ('faculty_email', models.EmailField(max_length=254)),
                ('section', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date added')),
            ],
            options={
                'verbose_name_plural': 'Class Room',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(max_length=50)),
                ('no_of_semesters', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('department_name', models.CharField(max_length=10, unique=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.course')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('laboratory_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MCQ_Question',
            fields=[
                ('primary_key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('question', models.TextField(verbose_name='Question')),
                ('solution', models.TextField(blank=True, null=True, verbose_name='Solution')),
                ('ans1', models.TextField(verbose_name='Option 1')),
                ('ans_image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Option 1 image')),
                ('ans2', models.TextField(verbose_name='Option 2')),
                ('ans_image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Option 2 image')),
                ('ans3', models.TextField(verbose_name='Option 3')),
                ('ans_image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Option 3 image')),
                ('ans4', models.TextField(verbose_name='Option 4')),
                ('ans_image4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Option 4 image')),
                ('correct', models.IntegerField(verbose_name='Correct Choice')),
                ('developer', models.CharField(blank=True, max_length=250, null=True, verbose_name='Developer name')),
                ('q_image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Question image 1')),
                ('q_image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Question image 2')),
                ('q_image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Question image 3')),
                ('a_image1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Answer image 1')),
                ('a_image2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Answer image 2')),
                ('a_image3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Answer image 3')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Date added')),
                ('reports', models.IntegerField(default=0, verbose_name='Error reports')),
                ('classroom_code', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='department.classroom')),
            ],
            options={
                'verbose_name_plural': 'MCQ Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('title', models.CharField(max_length=256, verbose_name='Name of quiz')),
                ('type', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=256, verbose_name='Type of quiz')),
                ('maximum_marks', models.IntegerField(verbose_name='Total marks of quiz')),
                ('minimum_marks', models.IntegerField(null=True, verbose_name='Passing marks of quiz')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Date added')),
                ('duration', models.FloatField(blank=True, default='', null=True, verbose_name='Duration in hours')),
                ('primary_key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('classroom_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('subject_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Subjective_Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('Very Short Answer', 'Very Short Answer'), ('Short Answer', 'Short Answer'), ('Long Answer', 'Long Answer')], max_length=50, verbose_name='Type of Question')),
                ('question', models.TextField()),
                ('solution', models.TextField(blank=True, null=True)),
                ('q_image1', models.ImageField(blank=True, null=True, upload_to='questions/images', verbose_name='Question image 1')),
                ('q_image2', models.ImageField(blank=True, null=True, upload_to='questions/images', verbose_name='Question image 2')),
                ('q_image3', models.ImageField(blank=True, null=True, upload_to='questions/images', verbose_name='Question image 3')),
                ('a_image1', models.ImageField(blank=True, null=True, upload_to='questions/images', verbose_name='Answer image 1')),
                ('a_image2', models.ImageField(blank=True, null=True, upload_to='questions/images', verbose_name='Answer image 2')),
                ('a_image3', models.ImageField(blank=True, null=True, upload_to='questions/images', verbose_name='Answer image 3')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Date added')),
                ('reports', models.IntegerField(default=0, verbose_name='Error reports')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('classroom_code', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='department.classroom')),
            ],
            options={
                'verbose_name_plural': 'Subjective Questions',
            },
        ),
        migrations.CreateModel(
            name='SubjectiveQuestionsQuiz',
            fields=[
                ('primary_key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.subjective_questions')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='MCQ_QuestionsQuiz',
            fields=[
                ('primary_key', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.mcq_question')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentLaboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.laboratory')),
            ],
        ),
    ]
