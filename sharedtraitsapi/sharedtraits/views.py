from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import UserAnswerModel
from .models import QuestionModel

from .serializers import UserAnswerModelSerializer
from .serializers import QuestionModelSerializer

class ListUserAnswers(generics.ListCreateAPIView):
    queryset = UserAnswerModel.objects.all()
    serializer_class = UserAnswerModelSerializer
    
#Fix csrf issues, do not leave as csrf_exempt
@csrf_exempt
def PostUserAnswers(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_class = UserAnswerModelSerializer(data=data)

        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse(serializer_class.data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailUserAnswers(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswerModel.objects.all()
    serializer_class = UserAnswerModelSerializer

#Fix csrf issues, do not leave as csrf_exempt
@csrf_exempt
def ListQuestions(request, id):
    if request.method == 'GET':
        question = QuestionModel.objects.all()[id-1]
        serializer_class = QuestionModelSerializer(question)

        return JsonResponse(serializer_class.data, status=status.HTTP_200_OK)
# class ListQuestions(generics.ListCreateAPIView, id):
#     queryset = QuestionModel.objects.all()
#     serializer_class = QuestionModelSerializer

class DetailQuestions(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionModelSerializer