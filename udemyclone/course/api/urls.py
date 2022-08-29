from django.urls import include,path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'courses',views.CourseViewSet)
router.register(r'tabs',views.TabViewSet)
router.register(r'categories', views.CategoryViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('logout',view=views.LogoutView.as_view()),
]




