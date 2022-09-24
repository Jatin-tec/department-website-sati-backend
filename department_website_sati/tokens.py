import json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from faculty.models import ContactDetails
# from rest_framework_simplejwt.token import TokenObtainPairView
from student.models import Student

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attr):
        data = super().validate(attr)
        token = self.get_token(self.user)
        
        if(self.user.role == 'teacher'):
            userProfile = ContactDetails.objects.get(user=self.user)
            profile = {
                'facultyId': userProfile.faculty_id,
                'adharNo': userProfile.adhar_no,
                'firstName': self.user.first_name,
                'lastName': self.user.last_name,
                'designation': userProfile.designation,
                'phone': userProfile.mobile_no,
                'email': self.user.email, 
                'role': 'teacher'
            }
            profile_str = json.dumps(profile)
            data['profile'] = profile_str

        if(self.user.role == 'student'):
            userProfile = Student.objects.get(user=self.user)
            profile = {
                'scholarNumber': userProfile.scholar_no,
                'firstName': self.user.first_name,
                'lastName': self.user.last_name,
                'email': self.user.email, 
                'enrollmentNo': userProfile.enrollment_no,
                'role': 'student'
            }
            profile_str = json.dumps(profile)
            data['profile'] = profile_str
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer