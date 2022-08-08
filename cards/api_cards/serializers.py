from rest_framework import serializers
from .models import MemoryCard


class MemoryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryCard
        fields = ['question', 'answer']
