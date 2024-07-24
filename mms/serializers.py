from rest_framework.serializers import ModelSerializer
from .models import *
from Account.models import User
from mess_name.models import Mess


class MessSerializer(ModelSerializer):
    class Meta:
        model = Mess
        fields = "__all__"


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


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'],
                    email=validated_data['email']
                    )
        user.set_password(raw_password=validated_data['password'])
        user.save()

        return user


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "nid",
            "phone",
            "dept",
            "district",
            "division",
            "created",
            "updated",
            "sts",
            "mess",
            "account",
            "username",
            "email",
            "room_num",
        ]


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "username",
            "tk",
            "month",
            "is_paid",
            "room_num",
            "time"
        ]
