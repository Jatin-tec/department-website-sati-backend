from dataclasses import field
from pyexpat import model
from re import S
from statistics import mode
from rest_framework import serializers 
from department.models import Course, Department, Branch, Subject, ClassRoom, Subjective_Questions, MCQ_Question, Assingment, Quiz, SubjectiveQuestionsQuiz, MCQ_QuestionsQuiz
from rest_framework.reverse import reverse

class CourseSerializer(serializers.ModelSerializer):
    # edit_url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='course-detail',
    #     lookup_field='course_id'
    # )
    
    class Meta:
        model = Course
        fields = [
            # 'url',
            # 'edit_url',
            'course_id',
            'course_name',
            'no_of_semesters',           
        ]

    # def get_edit_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("course-update", kwargs={"course_id":obj.course_id}, request=request)   

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            # 'url',
            # 'edit_url',
            'department_id',
            'department_name',
            'course_id',
            'hod_faculty'           
        ]

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = [
            # 'url',
            # 'edit_url',
            'branch_id',
            'branch_name',
            'department_id',          
        ]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            # 'url',
            # 'edit_url',
            'subject_id',
            'subject_name',
            # 'branch_id',          
        ]

from student.serializers import StudentSerializer    
from student.models import Student
from department.models import CustomUser

class ClassRoomSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True, read_only=False)
    class Meta:
        model = ClassRoom
        fields = [
            'classroom_code',
            'class_name',
            'faculty_email', 
            'faculty_id',
            'subject',        
            'branch',
            'section',
            'students'
        ]

    def create(self, validated_data):
        students = validated_data.pop('students')
        classroom = ClassRoom.objects.create(**validated_data)
        return classroom

    def update(self, instance, validated_data):
        students = validated_data.pop('students')
        instance = super(ClassRoomSerializer, self).update(instance, validated_data)
    
        students_qs = Student.objects.all()
        print(validated_data, 'this this this')
        existing_students = [s for s in instance.students.all()]

        print(students)

        if Student.objects.filter(user=students[0]).exists():
            existing_students.append(Student.objects.get(user=students[0]))
            instance.students.set(existing_students)

        return instance

class GetClassRoomSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = ClassRoom
        fields = [
            'classroom_code',
            'faculty_id',
            'subject',        
            'class_name',
            'branch',
            'section',
            'faculty_email', 
            'students'    
        ]

class SubjectiveQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjective_Questions
        fields = [
            # 'url',
            # 'edit_url',
            'classroom_code',
            'question_type',
            'question',
            'solution',

            'q_image1',
            'q_image2',
            'q_image3',

            'a_image1',
            'a_image2',
            'a_image3',
        ]

class MCQ_QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQ_Question
        fields = [
            # 'url',
            # 'edit_url',
            'classroom_code',
            'question',
            'solution',
            
            'ans1',
            'ans_image1',
            'ans2',
            'ans_image2',
            'ans3',
            'ans_image3',
            'ans4',
            'ans_image4',

            'correct',
            'developer',

            'q_image1',
            'q_image2',
            'q_image3',

            'a_image1',
            'a_image2',
            'a_image3',
        ]

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = [
            # 'url',
            # 'edit_url',
            'primary_key',
            'classroom_code',
            'title',
            'type',
            'maximum_marks',
            'minimum_marks',
            'duration',

        ]        

class AssingmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assingment
        fields = [
            # 'url', 
            # 'edit_url',
            'classroom_code',
            'question',
            'assingment_file',
            'image',
            'maximum_marks',
            'due_date',
        ]

class SubjectiveQuestionsQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectiveQuestionsQuiz
        fields = [
            # 'url', 
            # 'edit_url',
            'quiz_id',
            'question_id'
        ]

class MCQ_QuestionsQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQ_QuestionsQuiz
        fields = [
            # 'url', 
            # 'edit_url',
            'quiz_id',
            'question_id'
        ]

class RegisterUserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}   
        

    def create(self, validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance         