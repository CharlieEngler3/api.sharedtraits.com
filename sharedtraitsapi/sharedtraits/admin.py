from django.contrib import admin

from .models import CustomUser
from .models import UserAnswerModel
from .models import QuestionModel

admin.site.register(CustomUser)
admin.site.register(UserAnswerModel)
admin.site.register(QuestionModel)