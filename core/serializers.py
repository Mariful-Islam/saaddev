from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import User



class SignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'product']
        extra_kwargs = {'password': {'write_only': True}}

        
    def create(self, validated_data):
        
        user = User(username = validated_data['username'],
                    email = validated_data['email'],
                    product = validated_data['product']
                    )
        user.set_password(raw_password=validated_data['password'])
        user.save()
        
        return user
