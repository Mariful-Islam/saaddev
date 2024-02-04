from django.db import models
from django.contrib.auth.models import AbstractUser
from Account.models import User
from mess_name.models import Mess


# Create your models here.


class Student(models.Model):
    mess = models.ForeignKey(Mess, on_delete=models.CASCADE)
    account = models.OneToOneField(User, on_delete=models.CASCADE)
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

    def room_num(self):
        rooms = self.room_set.all()
        for room in rooms:
            room_number = room.room_number
            return room_number

    def get_date_created(self):
        day = str(self.created)[8:10]
        month = str(self.created)[5:7]
        year = str(self.created)[0:4]

        date = []

        if int(month) == 1:
            month = "Jan"
        elif int(month) == 2:
            month = "Feb"
        elif int(month) == 3:
            month = "Mar"
        elif int(month) == 4:
            month = "Apr"
        elif int(month) == 5:
            month = "May"
        elif int(month) == 6:
            month = "Jun"
        elif int(month) == 7:
            month = "Jul"
        elif int(month) == 8:
            month = "Aug"
        elif int(month) == 9:
            month = "Sep"
        elif int(month) == 10:
            month = "Oct"
        elif int(month) == 11:
            month = "Nov"
        elif int(month) == 12:
            month = "Dec"

        date.append(day)
        date.append(month)
        date.append(year)

        newdate = " ".join(date)

        return newdate

    def get_time_created(self):
        hour = str(self.created)[11:13]
        bd_hour = int(hour) + 6

        min = str(self.created)[13:16]

        if bd_hour < 12:
            time = str(bd_hour) + min + " AM"
        elif bd_hour == 12:
            time = str(bd_hour) + min + " PM"
        elif bd_hour > 12:
            bd_hour_pm = bd_hour - 12
            time = str(bd_hour_pm) + min + " PM"

        return time

    def get_date_updated(self):
        day = str(self.updated)[8:10]
        month = str(self.updated)[5:7]
        year = str(self.updated)[0:4]

        date = []

        if int(month) == 1:
            month = "Jan"
        elif int(month) == 2:
            month = "Feb"
        elif int(month) == 3:
            month = "Mar"
        elif int(month) == 4:
            month = "Apr"
        elif int(month) == 5:
            month = "May"
        elif int(month) == 6:
            month = "Jun"
        elif int(month) == 7:
            month = "Jul"
        elif int(month) == 8:
            month = "Aug"
        elif int(month) == 9:
            month = "Sep"
        elif int(month) == 10:
            month = "Oct"
        elif int(month) == 11:
            month = "Nov"
        elif int(month) == 12:
            month = "Dec"

        date.append(day)
        date.append(month)
        date.append(year)

        newdate = " ".join(date)

        return newdate

    def get_time_updated(self):
        hour = str(self.updated)[11:13]
        bd_hour = int(hour) + 6

        min = str(self.updated)[13:16]

        if bd_hour < 12:
            time = str(bd_hour) + min + " AM"
        elif bd_hour == 12:
            time = str(bd_hour) + min + " PM"
        elif bd_hour > 12:
            bd_hour_pm = bd_hour - 12
            time = str(bd_hour_pm) + min + " PM"

        return time


class Room(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room_number = models.IntegerField()

    def __str__(self) -> str:
        return str(self.room_number)

    def username(self):
        return self.student.account.username

    def sts(self):
        return self.student.sts


class Floor(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.number

    def student_name(self):
        return self.student.account.username

    def room_number(self):
        return self.room.room_number


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    month = models.CharField(max_length=100)
    tk = models.FloatField(max_length=100)
    is_paid = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.room.student.account.username

    def username(self):
        return self.student.account.username

    def room_num(self):
        return self.room.room_number

    def get_date(self):

        day = str(self.time)[8:10]
        month = str(self.time)[5:7]
        year = str(self.time)[0:4]

        date = []

        if int(month) == 1:
            month = "Jan"
        elif int(month) == 2:
            month = "Feb"
        elif int(month) == 3:
            month = "Mar"
        elif int(month) == 4:
            month = "Apr"
        elif int(month) == 5:
            month = "May"
        elif int(month) == 6:
            month = "Jun"
        elif int(month) == 7:
            month = "Jul"
        elif int(month) == 8:
            month = "Aug"
        elif int(month) == 9:
            month = "Sep"
        elif int(month) == 10:
            month = "Oct"
        elif int(month) == 11:
            month = "Nov"
        elif int(month) == 12:
            month = "Dec"

        date.append(day)
        date.append(month)
        date.append(year)

        newdate = " ".join(date)

        return newdate

    def get_time(self):

        hour = str(self.time)[11:13]
        bd_hour = int(hour) + 6

        min = str(self.time)[13:16]

        if bd_hour < 12:
            time = str(bd_hour) + min + " AM"
        elif bd_hour == 12:
            time = str(bd_hour) + min + " PM"
        elif bd_hour > 12:
            bd_hour_pm = bd_hour - 12
            time = str(bd_hour_pm) + min + " PM"

        return time
