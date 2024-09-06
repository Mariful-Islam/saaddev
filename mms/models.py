from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import User
from mess_name.models import Mess


# Create your models here.


class Student(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE)
    room_num = models.CharField(max_length=100, blank=True, null=True)
    nid = models.IntegerField()
    phone = models.IntegerField()
    dept = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    division = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    sts = models.CharField(max_length=100, default='active')

    def __str__(self) -> str:
        return self.account.username

    def username(self):
        return self.account.username

    def email(self):
        return self.account.email


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.CharField(max_length=100)
    tk = models.FloatField(max_length=100)
    is_paid = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.student.account.username

    def username(self):
        return self.student.account.username
    
    def room_num(self):
        return self.student.room_num

    
