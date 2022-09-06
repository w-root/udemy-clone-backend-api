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
        
        
# Course Serializers
class CourseSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True,read_only=True)
    instructor = serializers.StringRelatedField(read_only=True)
    image = serializers.ImageField(read_only=True)
      
    class Meta:
        model = Course
        fields = '__all__'
        
class CourseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['image']
        
        
# Profile Serializers
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    photo = serializers.ImageField(read_only=True)
    firstname = serializers.SerializerMethodField()
    lastname = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = '__all__'     

    def get_firstname(self,obj):
        return obj.user.first_name
    
    def get_lastname(self,obj):
        return obj.user.last_name

class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['photo']