from rest_framework.viewsets import ModelViewSet
from ..models import Category,Course, Tab
from .serializers import CourseSerializer,CategorySerializer, TabSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'

class TabViewSet(ModelViewSet):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
