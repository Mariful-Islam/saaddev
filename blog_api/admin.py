from django.contrib import admin
from blog_api.models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)