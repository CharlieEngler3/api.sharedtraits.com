from django.urls import path

from . import views

urlpatterns = [
    path('useranswers', views.ListUserAnswers.as_view()),
    path('useranswers/add', views.PostUserAnswers),
    path('<int:pk>', views.DetailUserAnswers.as_view()),
    path('questions/<int:id>', views.ListQuestions),
    path('<int:pk>', views.DetailQuestions.as_view()),
]