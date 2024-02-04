from django.db import models
from Account.models import User



class Transfer(models.Model):
    account_id = models.CharField(max_length=20)
    amount = models.FloatField()
    tran_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = BankAccount.objects.get(
            account_id=self.account_id).user.username
        return username

    def username(self):
        username = BankAccount.objects.get(
            account_id=self.account_id).user.username
        return username


class Ledger(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    amount = models.FloatField()
    transaction_id = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender

    class Meta:
        ordering = ['-time']
    
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
        bd_hour = int(hour)+6

        min = str(self.time)[13:16]

        if bd_hour < 12:
            time = str(bd_hour) + min + " AM"
        elif bd_hour == 12:
            time = str(bd_hour) + min + " PM"
        elif bd_hour > 12:
            bd_hour_pm = bd_hour - 12 
            time = str(bd_hour_pm) + min + " PM"

        return time
    


class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_id = models.CharField(max_length=20, unique=True)
    balance = models.FloatField()

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_name(self):
        return self.user.name

    def get_email(self):
        return self.user.email

    def get_avater(self):
        return self.user.avater.url

    def get_account_id(self):
        account = BankAccount.objects.get(user=self.user)
        account_id = account.account_id
        return account_id

    def get_balance(self):
        account = BankAccount.objects.get(user=self.user)
        balance = account.balance
        return balance


class Revenue(models.Model):
    revenue = models.FloatField()
    gas_fee = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        revenue = str(self.revenue)
        return revenue

    def get_per_month_revenue(self):
        res = []
        for i in range(1, 12):
            r = Revenue.objects.filter(date__month=(i))
            res.append(r)

        return res

    def get_per_day_revenue(self):
        day = Revenue.objects.filter(date__year=(
            2023), date__month=(10), date__day=(5))
        return day
