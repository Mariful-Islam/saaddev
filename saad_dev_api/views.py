import json
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ServiceSerializer, ProjectSerializer, ProjectStatsticSerializer, ClientSerializer, PartnershipSerializer, ContactSerializer, WebMailSerializer
from base.utils import get_mail
from base.models import Client, Partnership, Project, Contact, ProjectStatstic, Service, WebMail
from django.core.mail import send_mail
from django.conf import settings

@api_view(['GET'])
def services(request):
    
    services = Service.objects.all()
    
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def service(request, id):
    service = Service.objects.get(id=id)

    serializer = ServiceSerializer(service, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def service_component(request):
    
    services = Service.objects.all()[0:3]
    
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def projects(request):
    
    projects = Project.objects.all()
    
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project(request, id):
    project = Project.objects.get(id=id)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def project_component(request):
    
    projects = Project.objects.all()[0:3]
    
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def projects_stats(request):
    
    projects = ProjectStatstic.objects.all()
    
    serializer = ProjectStatsticSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def clients(request):
    
    clients = Client.objects.all()
    
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def partnerships(request):
    
    partnerships = Partnership.objects.all()
    
    serializer = PartnershipSerializer(partnerships, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def contact_api(request):
    if request.method == "POST":
        

        # spam_keywords = ['lottery', 'lottary', 'prise', 'prize', 'win', 'cash']
        # for i in range(0, len(spam_keywords)):
        #     print(spam_keywords[i])
        #     if spam_keywords[i] in username.lower() or email.lower() or subject.lower() or message.lower():
        #         category = 4
        username = request.data['username']
        email = request.data['email']
        subject = request.data['subject']
        message = request.data['message']

        subject = subject
        message = f"Name: {username} \nEmail: {email} \nMessage\n{message}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]

        send_mail(subject, message, email_from, recipient_list)
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
            return Response("Your mail sent to SaadDev.")
    return Response("Your mail sent to SaadDev.")


@api_view(['GET', 'POST'])
def mail(request):
    get_mail(request)
    message = Contact.objects.all()
    
    serializer = ContactSerializer(message, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def mail_write(request):
    if request.method == "POST": 
        email = request.data['email']
        subject = request.data['subject']
        message = request.data['message']
        category = request.data['category']
        user = Contact.objects.filter(email=email)[0]

        
        write = Contact.objects.create(username=user.username,
                                       email=email,
                                       subject=subject, 
                                       message=message,
                                       category=category)
        
        

        # if write.is_valid():
        #     if request.body['type'] == "sent":
        #         write.category = 2
        #         write.save()
        #         return Response("Sent")
        #     elif request.body['type'] == "draft":
        #         write.category = 3
        #         write.save()
        #         return Response("Saved")

    return Response("procesing")


@api_view(['GET'])
def mail_view(request, id):
    mail = Contact.objects.get(id=id)
    serializer = ContactSerializer(mail, many=False)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def mail_dlt(request, id):
    mail = Contact.objects.get(id=id)
    mail.delete()
    return Response('Deleted')



@api_view(['GET'])
def web_mail_auth(request, username, password):

    try:
        auth = WebMail.objects.get(username=username, password=password) 
        serializer = WebMailSerializer(auth, many=False)
        return Response(serializer.data)
    except:
        return Response("Not Authenticated")


@api_view(['GET', 'POST'])
def create_auth(request):
    if request.method == "POST":
        api_username = request.data['username']
    
        api_email = request.data['email']
        api_password = request.data['password']
        print(api_username, api_email, api_password)

        try:
            try:
                db_username = WebMail.objects.get(username=api_username).username
                if db_username == api_username:
                    return Response("Username is already exist")
                
            except:
                db_email = WebMail.objects.get(username=api_email).email
                db_password = WebMail.objects.get(username=api_password).password
                if db_email == api_email:
                        return Response("Email is already exist")
                elif db_password == api_password:
                    return Response("password is already exist")
                
                else:
                    serializer = WebMailSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response("Authenicated")
                        
        except:
            return Response("Not Authenicated")                
            
    return Response("")


@api_view(['GET', 'PUT'])
def update_auth(request):
    auth = WebMail.objects.get(id=1)

    if request.method == "PUT":
    #     username = request.data['username']
    #     password = request.data['password']
        
        serializer = WebMailSerializer(instance=auth, data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated')
    return Response()


