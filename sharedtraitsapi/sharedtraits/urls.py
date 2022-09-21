from django.urls import path

from knox import views as knox_views

from . import views

urlpatterns = [
    path('register', views.RegisterUser),
    path('login', views.LogInUser),
    path('logout', knox_views.LogoutView.as_view()),
    path('getuser', views.GetUser),
    path('showusers', views.ListUsers.as_view()),

    path('useranswers', views.ListUserAnswers.as_view()),
    path('useranswers/add', views.PostUserAnswers),
    path('<int:pk>', views.DetailUserAnswers.as_view()),
    
    path('questions', views.GetQuestions),
    path('<int:pk>', views.DetailQuestions.as_view()),
]