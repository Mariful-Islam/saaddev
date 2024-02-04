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
            'id',
            'mess',
            'account',
            'nid',
            'phone',
            'dept',
            'district',
            'division',
            'username',
            'sts',
            'email',
            'room_num',
            'get_date_created',
            'get_time_created',
            'get_date_updated',
            'get_time_updated'
        ]


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'student',
            'username',
            'room_number',
            'sts'
        ]


class FloorSerializer(ModelSerializer):
    class Meta:
        model = Floor
        fields = [
            "id",
            "student",
            "room",
            "student_name",
            "room_number",
        ]


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "username",
            "room_num",
            "tk",
            "month",
            "is_paid",
            "get_date",
            "get_time",
        ]
