from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'dept', 'district')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_paid')
