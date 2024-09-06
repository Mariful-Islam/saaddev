from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import json

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == "POST":
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        product = request.data['product']

        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        user = None
        if not user:
            user = authenticate(email=email, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'username': username, 'token': token.key}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response()


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.get(email=email)

        user = None
        if not user:
            user = authenticate(email=email, password=password)
            print(user)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'username': user.username, 'userId': user.id, 'token': token.key}, status=status.HTTP_200_OK)

        return Response('Invalid Credintial', status=status.HTTP_401_UNAUTHORIZED)
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == "POST":
        try:
            request.user.authtoken_token.delete()
            return Response({'message': 'Successfully Log Out'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'erroe': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def token_verify(request):
    if request.method == "POST":
        token = request.data['token']
        try:
            token = Token.objects.get(key=token)
            return Response(True)        
        except:
            return Response("Token not match or empty", status=status.HTTP_401_UNAUTHORIZED)
    return Response(False)
        
            
@api_view(['GET'])
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
        serializer = SignUpSerializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response("Error fetch user", status=status.HTTP_404_NOT_FOUND)

