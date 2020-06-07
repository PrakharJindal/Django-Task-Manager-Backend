from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LoginSerializer,  SignUpSerializer, AddTodoSerializer, TodoSerializer, TypeSerializer
from django.contrib.auth import login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate         # for Token Authentication
from rest_framework.authtoken.models import Token    # for Token Authentication
from django.views.decorators.csrf import csrf_exempt  # for Token Authentication
from rest_framework.authtoken.views import ObtainAuthToken  # for Token Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response            # for sending responses
from rest_framework.views import exception_handler

from rest_framework import status

from .models import Todo, Types
# Create your views here.


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "id": user.id})


class SignupView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            typeList = Types.objects.all()
            if not typeList:
                print('yesss')
                a1 = Types(typeName="General")
                a1.save()
                a2 = Types(typeName="Personal")
                a2.save()
                a3 = Types(typeName="Work")
                a3.save()
                a4 = Types(typeName="Others")
                a4.save()
                a1.user.add(user)
                a2.user.add(user)
                a3.user.add(user)
                a4.user.add(user)
            else:
                a1 = Types.objects.filter(typeName="General")
                a2 = Types.objects.filter(typeName="Personal")
                a3 = Types.objects.filter(typeName="Work")
                a4 = Types.objects.filter(typeName="Others")
                a1.user.add(user)
                a2.user.add(user)
                a3.user.add(user)
                a4.user.add(user)
            return Response({"token": token.key, "id": user.id})
        else:
            return Response(serializer.errors, status=200)
        # return Response({"erreo"})


class LogoutView(APIView):

    def post(self, request):
        logout(request)
        return Response(status=204)


class AddTodoView(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddTodoSerializer(data=request.data)

        print(request.data)

        if serializer.is_valid():
            instance = serializer.save()
            instance.user = request.user
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getTodos(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Todo.objects.filter(user=id)

        except Todo.DoesNotExist:
            return Response({'No Data'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        todos = self.get_object(id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class editTodo(APIView):
    authentication_classes = [TokenAuthentication]

    def get_object(self, id):
        try:
            return Todo.objects.get(id=id)

        except Todo.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        todos = self.get_object(id)
        serializer = TodoSerializer(todos, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getTypes(APIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Types.objects.filter(user=id)

        except Todo.DoesNotExist:
            return Response({'No Data'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = TypeSerializer(article, many=True)
        # if serializer.is_valid():
        #     print("ok")
        return Response(serializer.data, status=200)
        # return Response({"no data"})


class addType(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        # serializer = TypeSerializer(data =request)
        # if serializer.is_valid():
        #     instance = serializer.save()
        #     instance.user.add(request.user)
        #     instance.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        a = Types(typeName=request.data["typeName"])
        a.save()
        a.user.add(request.user)
        return Response("Complete", status=status.HTTP_201_CREATED)


class getUserDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        print(request.user.id)
        if(request.user.id == id):
            username = request.user.username
            email = request.user.email
            return Response({"username": username, "email": email}, status=200)
        return Response({'status': "No Data"}, status=status.HTTP_204_NO_CONTENT)
