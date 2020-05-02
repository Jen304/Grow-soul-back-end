from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone


from .models import Emotion
from .serializers import EmotionSerializer, EmotionUpdateSerialiser


class EmotionList(generics.ListCreateAPIView):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer


class EmotionDetail(generics.RetrieveUpdateAPIView):
    queryset = Emotion.objects.all()
    serializer_class = EmotionUpdateSerialiser


class EmotionTimeRange(generics.ListAPIView):
    serializer_class = EmotionSerializer

    def get_queryset(self):
        start_time = self.kwargs['start']
        start_time = timezone.strptime(
            self.kwargs['start'], '%Y-%m-%dT%H:%M:%S')
        end_time = timezone.strptime(
            self.kwargs['end'], '%Y-%m-%dT%H:%M:%S')
        print(start_time)
        return Emotion.objects.all()
