from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

from mess_name.models import Mess
from .serializers import MessSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def welcome(request):
    if request.method == "POST":
        mess_name = request.data['mess_name']
        location = request.data['location']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        setup = Mess.objects.create(mess_name=mess_name,
                                    location=location,
                                    owner=username,
                                    owner_email=email,
                                    password=password
                                    )
        return Response(f"{mess_name} setup completed.")

    return Response("")


@api_view(['GET', 'POST'])
def admin_login(request):
    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']

        try:
            mess_admin = Mess.objects.get(owner=username, password=password)
            return Response(json.dump({"username":username, "password":password}))

        except:
            return Response("Invalid Admin")

    return Response("")


@api_view(['GET', 'POST'])
def get_admin(request):
    if request.method == "POST":
        username = request.data['username']

        try:
            mess = Mess.objects.get(owner=username)
            return Response({"username": username})

        except:
            return Response("")
    return Response("")


@api_view(['GET'])
def get_mess(request, username):
    try:
        mess = Mess.objects.get(username=username)
        serializer = MessSerializer(mess, many=False)
        return Response(serializer.data)

    except:
        return Response("No Mess Registered", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_messes(request):
    mess = Mess.objects.all()
    serializers = MessSerializer(mess, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def get_all_admin(request):
    messes = Mess.objects.all()
    admin=[]
    for mess in messes:
        admin.append(mess.owner)

    return Response(admin)
