from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, null=True)
    avater = models.ImageField()
    product = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def image(self):
        return self.avater.url
    

class SEO(models.Model):
    meta_title = models.CharField(max_length=250, blank=True, null=True, unique=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

