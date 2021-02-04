from rest_framework import serializers
from .models import Performer

class PerformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performer
        fields = ('id', 'name', 'url', 'gender', 'aliases', 'favorite')
