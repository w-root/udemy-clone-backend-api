from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify
from PIL import Image
from ckeditor.fields import RichTextField

# Create your models here.
class Tab(models.Model):
    name = models.CharField(max_length=255)
    textTitle = models.CharField(max_length=255)
    textContent = models.TextField()
            
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True,unique=True,db_index = True,max_length=250,null=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)   
        
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    bio = RichTextField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True,default='profile_images/default_profile_image/user_default_profile_image.jpg',upload_to='profile_images/%Y/%m/')
    language = models.CharField(max_length=30,null=True, blank=True)
    website = models.CharField(max_length=75, null=True,blank=True)
    twitter = models.CharField(max_length=75, null=True,blank=True)
    facebook = models.CharField(max_length=75, null=True,blank=True)
    linkedin = models.CharField(max_length=75, null=True,blank=True)
    youtube = models.CharField(max_length=75, null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)       
        if self.photo:
            img = Image.open(self.photo.path) 
            output_size = (1000,1000) 
            img.thumbnail(output_size) 
            img.save(self.photo.path) 
     
class Course(models.Model):
    students = models.ManyToManyField(User,related_name='students')
    tabs = models.ForeignKey(Tab,on_delete=models.CASCADE,related_name='tab',null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='instructor',default=1)
    title = models.CharField(max_length=255,null=True,blank=True)
    subtitle = models.CharField(max_length=255,null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='course_images/%Y/%m/')
    releaseDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    price = models.DecimalField(decimal_places=2,max_digits=10,null=True,blank=True)
    rating = models.PositiveIntegerField(null=True,blank=True,default=5,validators=[MinValueValidator(1),MaxValueValidator(5)],)
    slug = models.SlugField(blank=True,unique=True,db_index = True,max_length=250,null=True)
    whatYouWillLearn = models.JSONField(null=True,blank=True,encoder=None)
    is_home = models.BooleanField(default=False,null=True,blank=True)
   
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)       
        if self.image:
            img = Image.open(self.image.path)
            output_size = (300,175) 
            img.thumbnail(output_size) 
            img.save(self.image.path)                 

    def __str__(self):
        return self.title