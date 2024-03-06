from django.db import models
from Account.models import User


class DeliveryPlace(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField()
    desc = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.product.name

    def username(self):
        return self.user.username

    def product_name(self):
        return self.product.name

    def product_image(self):
        return self.product.image.url

    def product_price(self):
        return self.product.price


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    delivery_place = models.ForeignKey(DeliveryPlace, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username

    def username(self):
        return self.user.username

    def product_name(self):
        return self.product.name

    def product_quantity(self):
        return self.quantity

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

    def get_delivery_place(self):
        return self.delivery_place.name

    def product_price(self):
        return self.product.price
