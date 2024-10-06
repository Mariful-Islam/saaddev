from django.db import models
from core.models import *
# Create your models here.



class Profile(SEO):
    view = models.OneToOneField(User, related_name="view", on_delete=models.CASCADE, null=True, blank=True)
    follower = models.OneToOneField(User, related_name="follower", on_delete=models.CASCADE, null=True, blank=True)
    following = models.OneToOneField(User, related_name="following", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self) -> str:
        return self.view.username


class Category(models.Model):
    category = models.JSONField()


class Post(SEO):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    tag = models.CharField(max_length=500, blank=True, null=True)
    views = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.description[0:50]
    
    @property
    def username(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

    def post_id(self):
        return self.post.id

    def post_title(self):
        return self.post.title
    
    def username(self):
        return self.user.username

