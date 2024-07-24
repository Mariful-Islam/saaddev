from django.db import models
from Account.models import User

# Create your models here.

# class BlogUser(User):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     username = models.CharField(max_length=100, unique=True, blank=True, null=True)
#     email = models.CharField(max_length=100, unique=True, blank=True, null=True)
#     avater = models.ImageField(blank=True, null=True)
#     followers = models.ForeignKey(User, on_delete=models.Case)
    



class Post(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=500)

    def __str__(self):
        return self.content[0:50]

    def tag_list(self):
        return self.tag.split(',')
    
    def update_time(self):
        return str(self.updated.today())


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

    def post_id(self):
        return self.post.id

    def post_title(self):
        return self.post.title

