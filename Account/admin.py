from django.contrib import admin

# Register your models here.
from Account.models import User

admin.site.register(User)