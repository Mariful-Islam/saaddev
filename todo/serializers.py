from rest_framework.serializers import ModelSerializer
from todo.models import *


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'desc', 'created', 'updated', 'get_count', 'get_date', 'get_time')
