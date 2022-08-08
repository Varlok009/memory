from rest_framework import generics
from .models import MemoryCard
from .serializers import MemoryCardSerializer


class MemoryCardAPIViews(generics.ListAPIView):
    queryset = MemoryCard.objects.all()
    serializer_class = MemoryCardSerializer
