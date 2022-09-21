from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication
from knox.models import AuthToken

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

from .models import CustomUser
from .models import UserAnswerModel
from .models import QuestionModel

from .serializers import UserSerializer
from .serializers import UserAnswerModelSerializer
from .serializers import QuestionModelSerializer



#Fix csrf issues, do not leave as csrf_exempt
@csrf_exempt
def RegisterUser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer_class = UserSerializer(data=data)

        if serializer_class.is_valid():
            user = serializer_class.save()

            token = AuthToken.objects.create(user)[1]

            return JsonResponse({"token": token, "userID": user.id}, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

#Fix csrf issues, do not leave as csrf_exempt
@csrf_exempt
def LogInUser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = None

        if data.get("email") != None:
            user = CustomUser.objects.get(email=data["email"])
        elif data.get("username") != None:
            user = CustomUser.objects.get(username=data["username"])
                
        serializer_class = UserSerializer(user)

        if check_password(data["password"], serializer_class.data["password"]):
            token = AuthToken.objects.create(user)[1]

            return JsonResponse({"token": token, "userID": user.id}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"error": "Wrong password my guy"}, status=status.HTTP_400_BAD_REQUEST)

#Fix csrf issues, do not leave as csrf_exempt
@csrf_exempt
def GetUser(request):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = None

        if data.get("email") != None:
            user = CustomUser.objects.get(email=data["email"])
        elif data.get("username") != None:
            user = CustomUser.objects.get(username=data["username"])
        elif data.get("userID") != None:
            user = CustomUser.objects.get(id=data["userID"])
        else:
            return JsonResponse({"error:": "User identification data not provided."}, status=status.HTTP_400_BAD_REQUEST)

        serializer_class = UserSerializer(user)

        packet = {
            "userID": serializer_class.data["id"],
            "email": serializer_class.data["email"],
            "username": serializer_class.data["username"],
            "tags": serializer_class.data["tags"],
        }

        return JsonResponse(packet, status=status.HTTP_200_OK)
        

class ListUsers(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class ListUserAnswers(generics.ListCreateAPIView):
    queryset = UserAnswerModel.objects.all()
    serializer_class = UserAnswerModelSerializer

class DetailUserAnswers(generics.RetrieveUpdateDestroyAPIView):
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



class DetailQuestions(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionModelSerializer

#Fix csrf issues, do not leave as csrf_exempt
#Also understand why you're using safe=False in the JsonResponse return statement
@csrf_exempt
def GetQuestions(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        question = None

        if data.get("questionID") != None:
            question = QuestionModel.objects.all()[data.get("questionID")-1]
            serializer_class = QuestionModelSerializer(question)
        elif data.get("tags") != None:
            tags = data.get("tags")

            questions = QuestionModel.objects.all()

            filtered_questions = None

            for tag in tags:
                filtered_questions += questions.filter(tags__tag=tag)

            serializer_class = QuestionModelSerializer(filtered_questions, many=True)
        else:
            questions = QuestionModel.objects.all()
            serializer_class = QuestionModelSerializer(questions, many=True)

        return JsonResponse(serializer_class.data, status=status.HTTP_200_OK, safe=False)