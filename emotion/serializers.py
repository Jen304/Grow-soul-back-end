from rest_framework import serializers
from .models import Emotion, User
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # print(validated_data)
        return User.objects.create_user(**validated_data)


'''
    # hash the password before store in the database
    def validate_password(self, value: str) -> str:

        return make_password(value)
'''


class EmotionSerializer(serializers.ModelSerializer):
    # created_at is optional field
    created_at = serializers.DateTimeField(
        required=False, default=timezone.now)

    class Meta:
        model = Emotion
        fields = '__all__'
        read_only_fields = ['user']
    # convert datetime data into timestamp
    '''
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["created_at"] = datetime.strftime(
            instance.created_at, '%Y-%m-%dT%H:%M:%S')
        return ret
    # validate created_at
    '''

    def validate(self, data):
        if data['created_at'] > timezone.now():
            raise serializers.ValidationError(
                "created_at should not be greater than current time")
        return data


class EmotionUpdateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = '__all__'
        # Update do not allow to change created_at
        read_only_fields = ['created_at', 'user']
