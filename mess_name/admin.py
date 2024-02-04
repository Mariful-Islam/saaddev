from django.contrib import admin
from .models import *


# Register your models here.

class MessAdmin(admin.ModelAdmin):
    list_display = ('mess_name', 'owner', 'location',)


admin.site.register(Mess, MessAdmin)
