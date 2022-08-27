from rest_framework import serializers
from ..models import Category,Course, Tab

class CourseSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = '__all__'   
                  
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        
