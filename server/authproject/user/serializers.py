from rest_framework import serializers
from .models import User, Student, Teacher
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'email', 'user_type']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'password', 'name', 'email', 'user_type', 'subscribed']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(StudentSerializer, self).create(validated_data)

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'password', 'name', 'email', 'user_type']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(TeacherSerializer, self).create(validated_data)
