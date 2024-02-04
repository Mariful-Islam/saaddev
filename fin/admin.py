from django.contrib import admin
from fin.models import *
# Register your models here.


class TransferAdmin(admin.ModelAdmin):
    list_display = ('username', 'account_id', 'amount')


admin.site.register(Transfer, TransferAdmin)


class LedgerAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'time')


admin.site.register(Ledger, LedgerAdmin)


class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'account_id', 'balance')


admin.site.register(BankAccount, BankAccountAdmin)


admin.site.register(Profile)
admin.site.register(Revenue)
