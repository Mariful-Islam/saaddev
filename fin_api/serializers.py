from rest_framework.serializers import ModelSerializer
from Account.models import User
from base.models import *
from django.contrib.auth.models import AbstractUser

from fin.models import BankAccount, Ledger, Profile, Revenue, Transfer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"


class LedgerSerializer(ModelSerializer):
    class Meta:
        model = Ledger
        fields = ["sender", "receiver", "transaction_id", "amount", "time", "get_date", "get_time"]


class BankAccountSerializer(ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ["id",
                  "account_id",
                  "balance", "get_username"]


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id",
                  "address",
                  "bio",
                  "user",
                  "get_username",
                  "get_name",
                  "get_email",
                  "get_avater"]


class RevenueSerializer(ModelSerializer):
    class Meta:
        model = Revenue
        fields = "__all__"


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        user = User(username = validated_data['username'],
                    email = validated_data['email']
                    )
        user.set_password(raw_password=validated_data['password'])
        user.save()
        
        return user


class AccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'last_login',
            'is_superuser',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'date_joined',
            'name',
            'username',
            'email',
            'avater',
            'groups',
            'image'
        ]