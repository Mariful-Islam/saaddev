import os
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Service, Project, Client, Partnership, ProjectStatstic, Contact
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

from .utils import get_mail


def home(request):
    services = Service.objects.all()[0:3]
    projects = Project.objects.all()[0:3]
    clients = Client.objects.all()

    context = {'services': services, 'projects': projects, 'clients': clients}
    return render(request, 'index.html', context)


def service(request):
    services = Service.objects.all()

    context = {'services': services}
    return render(request, 'service.html', context)


def single_service(request, service_name):
    service = Service.objects.get(name=service_name)

    context = {'service': service}
    return render(request, 'single-service.html', context)


def project(request):
    projects = Project.objects.all()
    project_statstics = ProjectStatstic.objects.all()

    context = {'projects': projects, 'project_statstics': project_statstics}
    return render(request, 'project.html', context)


def single_project(request, project_name):
    project = Project.objects.get(name=project_name)

    context = {'project': project}
    return render(request, 'single-project.html', context)


def client(request):
    clients = Client.objects.all()

    partnerships = Partnership.objects.all()

    context = {'clients': clients, 'partnerships': partnerships}
    return render(request, 'client.html', context)


def about(request):
    myprofile = Myprofile.objects.get(id=1)
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    context = {'myprofile': myprofile,
               'skills': skills, 'experiences': experiences}
    return render(request, 'about.html', context)


def contact(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        spam_keywords = ['lottery', 'lottary', 'prise', 'prize', 'win', 'cash']
        for i in range(0, len(spam_keywords)):
            print(spam_keywords[i])
            if spam_keywords[i] in username.lower() or email.lower() or subject.lower() or message.lower():
                category = 4

        contact = Contact.objects.create(
            username=username,
            email=email,
            subject=subject,
            message=message,
            category=category
        )

        contact.save()

    return render(request, 'contact.html')


def mail(request):
    context = get_mail(request)

    return render(request, 'mail.html', context)


def mail_view(request, id):
    context = get_mail(request)

    contacts = Contact.objects.all()
    contact = Contact.objects.get(id=id)

    context1 = {'contact': contact, 'contacts': contacts}
    context.update(context1)

    return render(request, 'mail-view.html', context)


def mail_delete(request, id):
    mail = Contact.objects.get(id=id)
    mail.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def mail_compose(request):
    if request.method == "POST":
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        try:
            username = Contact.objects.get(email=email).username
        except:
            username = email.split('@')[0]

        try:
            contact = Contact.objects.create(
                username=username,
                email=email,
                subject=subject,
                message=message,
                category=3)

            contact.save()
            messages.info(request, 'Email sent to {}'.format(username))
            return redirect('mail')

        except:
            contact = Contact.objects.create(
                username=username,
                email=email,
                subject=subject,
                message=message,
                category=2)
            contact.save()
            messages.info(
                request, 'Email not sent to {} but saved.'.format(username))
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    context = get_mail(request)

    return render(request, 'mail-compose.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/adminupload")
            response['content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response

    raise Http404
