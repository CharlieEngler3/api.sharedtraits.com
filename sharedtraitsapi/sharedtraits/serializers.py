from rest_framework import serializers
from .models import UserAnswerModel
from .models import QuestionModel

class UserAnswerModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'questionID',
            'answer',
        )
        model = UserAnswerModel

class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question',
            'answers',
        )
        model = QuestionModel
