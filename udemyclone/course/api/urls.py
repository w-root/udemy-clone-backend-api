from django.urls import include,path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'courses',views.CourseViewSet,basename='courses')
router.register(r'tabs',views.TabViewSet ,basename='tabs')
router.register(r'categories', views.CategoryViewSet ,basename='categories')

urlpatterns = [
    path('',include(router.urls)),
    path('logout',views.LogoutView.as_view(),name = 'logout'),
    path('instructor/courses',views.GetInstructorCoursesView.as_view(),name = 'instructor-courses'),
    path('courses/getbyid/<int:pk>',views.GetCourseById.as_view(),name = 'get-course-by-id'),
    path('student/courses',views.GetStudentsCoursesView.as_view(),name = 'student-courses'),
    path('student/buy-a-course',views.BuyACourseView.as_view(),name = 'buy-a-course'),
]




