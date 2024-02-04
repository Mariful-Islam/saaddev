from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ecom.models import *
from Account.models import User


class DeliveryPlaceSerializer(ModelSerializer):
    class Meta:
        model = DeliveryPlace
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id',
                  'user', 
                  'product', 
                  'quantity', 
                  'product_name', 
                  'product_image', 
                  'product_price',]
        


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


class SignUpSerializer(serializers.ModelSerializer):
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
    

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 
                  'user', 
                  'product', 
                  'product_name',
                  'quantity', 
                  'delivery_place', 
                  'time', 
                  'get_date', 
                  'get_time',
                  'get_delivery_place',
                  'product_price'
                  ]