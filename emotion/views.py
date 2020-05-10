from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone
from django.http import Http404, HttpResponseNotFound
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt import views as jwt_views


from .models import Emotion
from .serializers import EmotionSerializer, EmotionUpdateSerialiser, UserSerializer


class CreateUser(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class EmotionList(generics.ListCreateAPIView):
    model = Emotion
    serializer_class = EmotionSerializer

    def get_queryset(self):
        return Emotion.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmotionDetail(generics.RetrieveUpdateAPIView):

    def get_queryset(self):
        return Emotion.objects.filter(user=self.request.user)

    serializer_class = EmotionUpdateSerialiser

    def put(self, request, *args, **kwargs):
        # check the correct user
        emotion = Emotion.objects.get(pk=self.kwargs["pk"])
        if not request.user == emotion.user:
            raise PermissionDenied("It's not your emotion.")
        return super().put(request, *args, **kwargs)


class EmotionTimeRange(generics.ListAPIView):
    serializer_class = EmotionSerializer

    def get_queryset(self):
        try:
            '''
            start_time = self.kwargs['start']
            start_time = datetime.strptime(
                self.kwargs['start'], '%Y-%m-%dT%H:%M:%S-%z')
            end_time = datetime.strptime(
                self.kwargs['end'], '%Y-%m-%dT%H:%M:%S-%z')
            '''
            start_time = datetime.fromisoformat(self.kwargs['start'])
            end_time = datetime.fromisoformat(self.kwargs['end'])
            print(start_time)
            print(end_time)
            if(start_time > end_time):
                raise Http404(
                    'start date must be less then end date')
            return Emotion.objects.filter(created_at__range=[start_time, end_time], user=self.request.user)
        except:
            raise Http404(
                'date should be in iso correct format')


class Logout(APIView):
    permission_classes = ()

    def post(self, request):
        outdated_token = request.data.get('token')
        # print(outdated_token)
        token = RefreshToken(outdated_token)
        token.blacklist()
        return Response(status=status.HTTP_202_ACCEPTED)


class CustomObtainToken(jwt_views.TokenObtainPairView):
    permission_classes = ()


class CustomRefreshToken(jwt_views.TokenRefreshView):
    permission_classes = ()
