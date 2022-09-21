from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from .models import CustomUser
from .models import UserAnswerModel
from .models import QuestionModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'email',
            'username',
            'password',
            'tags',
        )
        model = CustomUser

    def create(self, validated_data):
        user = CustomUser(
            email = validated_data['email'],
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            tags = validated_data['tags'],
        )
        user.save()
        return user

class UserAnswerModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'userID',
            'questionID',
            'answerID',
        )
        model = UserAnswerModel

class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question',
            'answers',
            'tags',
        )
        model = QuestionModel