from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self) -> str:
        return self.name

    def get_count(self):
        count = Item.objects.all().count()
        return count
    
    def get_date(self):
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
    

    def get_time(self):
        hour = str(self.updated)[11:13]
        bd_hour = int(hour)+6

        min = str(self.updated)[13:16]

        if bd_hour < 12:
            time = str(bd_hour) + min + " AM"
        elif bd_hour == 12:
            time = str(bd_hour) + min + " PM"
        elif bd_hour > 12:
            bd_hour_pm = bd_hour - 12 
            time = str(bd_hour_pm) + min + " PM"

        return time
