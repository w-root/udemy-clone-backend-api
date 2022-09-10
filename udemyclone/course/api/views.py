from xml.etree.ElementInclude import include
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,UpdateAPIView,get_object_or_404
from rest_framework.response import Response
from ..models import Category,Course, Profile, Tab
from . import serializers
from rest_framework.authtoken.models import Token
from rest_framework import mixins

#Course Model Views # 
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    lookup_field ='slug'
       
    def perform_create(self, serializer):
        GetRequestUser(self.request)
        serializer.save(instructor=self.request.user)

class GetStudentsOrInstructorCoursesView(ListAPIView):
    serializer_class = serializers.CourseSerializer
    
    def get_queryset(self):
        if self.request.path.find("instructor/courses") != -1:
            username = self.kwargs.get('username')
            queryset = Course.objects.filter(instructor__username = username)
        elif self.request.path.find("student/courses") != -1:
            GetRequestUser(self.request)
            queryset = Course.objects.filter(students = self.request.user)       
        return queryset
      
class GetCourseById(ListAPIView):
    serializer_class = serializers.CourseSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Course.objects.get(id=pk)
        return queryset
        
class BuyACourseView(APIView):
    def post(self,request):
        GetRequestUser(request)
        for val in request.data:
            course = get_object_or_404(Course,id=val["id"])
            course.students.add(request.user)
        return Response("Kurs satın alındı !")    

class CourseImageUpdateView(UpdateAPIView): 
    serializer_class = serializers.CourseImageSerializer
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        instance = get_object_or_404(Course,id=pk)
        return instance

# Tab Model Views #
class TabViewSet(ModelViewSet):
    queryset = Tab.objects.all()
    serializer_class = serializers.TabSerializer

# Category Model Views #
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'

# User Model Views #
class UserProfilesViewSet(GenericViewSet,mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    
    def perform_update(self, serializer):
        user = GetRequestUser(self.request)
        if self.request.data["firstname"] and self.request.data["lastname"]:
            user.first_name = self.request.data["firstname"]
            user.last_name = self.request.data["lastname"]
        user.save()
        serializer.save()
    
class UserProfileView(APIView):
    def get(self,request,username):
        instance = Profile.objects.get(user__username = username)
        serializer = serializers.ProfileSerializer(instance)
        return Response(serializer.data) 
    
class LogoutView(APIView):
    def delete(self,request):
        GetRequestUser(request)
        request.user.auth_token.delete()
        return Response("Çıkış Yapıldı")

class ProfilePhotoUpdateView(UpdateAPIView): 
    serializer_class = serializers.ProfilePhotoSerializer
    
    def get_object(self):
        GetRequestUser(self.request)
        profile_instance = self.request.user.profile
        return profile_instance
 
    
def GetRequestUser(request):
    token = Token.objects.get(key = request.headers["Sessionid"])
    request.user = token.user
    return token.user