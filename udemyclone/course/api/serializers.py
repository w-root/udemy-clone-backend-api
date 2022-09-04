from rest_framework import serializers
from ..models import Category,Course, Profile, Tab
from django.contrib.auth.models import User

class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = '__all__'   
                  
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'     
           
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    photo = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Profile
        fields = '__all__'     
                
class CourseSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True,read_only=True)
    instructor = serializers.StringRelatedField(read_only=True)
      
    class Meta:
        model = Course
        fields = '__all__'


