from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = RichTextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    frontend = models.CharField(max_length=250, blank=True, null=True)
    backend = models.CharField(max_length=250, blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField()
    stack = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_stack_list(self):
        stacks = self.stack.split(',')
        return stacks

    def image_url(self):
        return self.image.url


class ProjectStatstic(models.Model):
    ONGOING_STATUS = 1
    COMPLETED_STATUS = 2
    STATUS_CHOICES = (
        (ONGOING_STATUS, 'Ongoing'),
        (COMPLETED_STATUS, 'Completed')
    )

    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=ONGOING_STATUS)

    def __str__(self):
        return self.project.name

    def get_project_name(self):
        return self.project.name

    def get_project_link(self):
        return self.project.link

    def get_status(self):
        if self.status == 1:
            return 'Ongoing'
        elif self.status == 2:
            return 'Completed'


class Client(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return self.name


class Partnership(models.Model):
    company_name = models.CharField(max_length=40)
    image = models.ImageField()

    def __str__(self):
        return self.company_name


class Contact(models.Model):
    INBOX_STATUS = 1
    DRAFT_STATUS = 2
    SENT_STATUS = 3
    SPAM_STATUS = 4

    STATUS_CHOICES = (
        (INBOX_STATUS, 'Inbox'),
        (DRAFT_STATUS, 'Draft'),
        (SENT_STATUS, 'Sent'),
        (SPAM_STATUS, 'Spam')
    )

    username = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(
        choices=STATUS_CHOICES, default=INBOX_STATUS)

    def __str__(self):
        return self.username

    def get_category(self):
        if self.category == 1:
            return 'Inbox'
        elif self.category == 2:
            return 'Draft'
        elif self.category == 3:
            return 'Sent'
        elif self.category == 4:
            return 'Spam'

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

    class Meta:
        ordering = ['-time']


class WebMail(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
