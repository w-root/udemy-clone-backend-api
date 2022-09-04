from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView,get_object_or_404
from rest_framework.response import Response
from ..models import Category,Course, Profile, Tab
from .serializers import CourseSerializer,CategorySerializer, ProfileSerializer, TabSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import mixins

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field ='slug'
       
    def perform_create(self, serializer):
        GetRequestUser(self.request)
        serializer.save(instructor=self.request.user)
        
class TabViewSet(ModelViewSet):
    queryset = Tab.objects.all()
    serializer_class = TabSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'        

class UserProfilesViewSet(GenericViewSet,mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class UserProfileView(APIView):
    def get(self,request,username):
        GetRequestUser(self.request)
        instance = Profile.objects.get(user = request.user)
        serializer = ProfileSerializer(instance)
        return Response(serializer.data) 
    
class LogoutView(APIView):
    def delete(self,request):
        GetRequestUser(request)
        request.user.auth_token.delete()
        return Response("Çıkış Yapıldı")

class GetInstructorCoursesView(ListAPIView):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        GetRequestUser(self.request)
        queryset = Course.objects.filter(instructor = self.request.user)
        return queryset
    
class GetStudentsCoursesView(ListAPIView):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        GetRequestUser(self.request)
        queryset = Course.objects.filter(students = self.request.user)
        return queryset
      
class GetCourseById(APIView):
    def get(self,request,pk):
        instance = Course.objects.get(id=pk)      
        serializer = CourseSerializer(instance)
        return Response(serializer.data)        

class BuyACourseView(APIView):
    def post(self,request):
        GetRequestUser(request)
        course = get_object_or_404(Course,id=request.data["id"])
        course.students.add(request.user)
        return Response("Kurs satın alındı !")
    
def GetRequestUser(request):
    token = Token.objects.get(key = request.headers["Sessionid"])
    request.user = token.user