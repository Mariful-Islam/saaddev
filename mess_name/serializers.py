from rest_framework.serializers import ModelSerializer
from .models import Mess


class MessSerializer(ModelSerializer):
    class Meta:
        model = Mess
        fields = "__all__"
