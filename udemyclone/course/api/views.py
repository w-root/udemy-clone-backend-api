from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Category,Course, Tab
from .serializers import CourseSerializer,CategorySerializer, TabSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


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

class LogoutView(APIView):
    def delete(self,request):
        GetRequestUser(request)
        request.user.auth_token.delete()
        return Response("Çıkış Yapıldı")
    
    
def GetRequestUser(request):
    token = Token.objects.get(key = request.headers["Sessionid"])
    request.user = token.user