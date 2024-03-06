from django.db import models


# Create your models here.

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

