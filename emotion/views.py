from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Emotion
from .serializers import EmotionSerializer


class EmotionList(APIView):
    def get(self, request):
        emotion = Emotion.objects.all()[:10]
        data = EmotionSerializer(emotion, many=True).data
        return Response(data)
