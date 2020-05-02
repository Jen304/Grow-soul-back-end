from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone
from django.http import Http404, HttpResponseNotFound


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
        try:
            start_time = self.kwargs['start']
            start_time = datetime.strptime(
                self.kwargs['start'], '%Y-%m-%dT%H:%M:%S')
            end_time = datetime.strptime(
                self.kwargs['end'], '%Y-%m-%dT%H:%M:%S')
            print(start_time)
            print(end_time)
            if(start_time > end_time):
                raise Http404(
                    'start date must be less then end date')
            return Emotion.objects.filter(created_at__range=[start_time, end_time])
        except:
            raise Http404(
                'date should be in correct format (%Y-%m-%dT%H:%M:%S)')
