from rest_framework import serializers
from student.models import Student
from department.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name'
        ] 

class StudentSerializer(serializers.ModelSerializer):
    # edit_url = serializers.SerializerMethodField(read_only=True)
    user = CustomUserSerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name='student-detail',
        lookup_field='scholar_no'
    )
    class Meta:
        model = Student
        fields = [
            'user',
            'scholar_no',
            'url',
            # 'edit_url',
            'enrollment_no',   
            'branch',     
        ]
        depth=2

    # def get_edit_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("student-update", kwargs={"scholar_no":obj.scholar_no}, request=request)   
