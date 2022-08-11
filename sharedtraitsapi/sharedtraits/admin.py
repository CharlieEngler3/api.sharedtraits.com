from django.contrib import admin

from .models import UserAnswerModel
from .models import QuestionModel

admin.site.register(UserAnswerModel)
admin.site.register(QuestionModel)