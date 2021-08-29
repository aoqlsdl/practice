from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import NullBooleanField

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
#     image = models.ImageField(upload_to = 'images/', blank = True, Null = True)

#     def __str__(self):
#         return self.title

# class PhotoInline(admin.TabularInline):
#     model = Photo

# class PostAdmin(admin.ModelAdmin):
#     inlines = [PhotoInline, ]

# admin.site.register(Post, PostAdmin)