from django.contrib import admin

from .models import Category, Course, Profile, Tab

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Tab)
admin.site.register(Profile)