from django.db import models


# Create your models here.


class Mess(models.Model):
    mess_name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    owner = models.CharField(max_length=100)
    owner_email = models.EmailField()
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.mess_name
