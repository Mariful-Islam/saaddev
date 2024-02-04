from django.urls import path
from saad_dev_api.views import contact_api, mail_dlt, mail_view, mail_write, project_component, service_component, services, projects, projects_stats, clients, partnerships, mail, web_mail_auth, update_auth, create_auth 

urlpatterns = [
    path('services/', services),
    path('service_component/', service_component),
    path('projects/', projects),
    path('project_component/', project_component),
    path('project-statstic/', projects_stats),
    path('clients/', clients),
    path('partnerships/', partnerships),
    path('contact_api/', contact_api),
    path('mails/', mail),
    path('mail_write/', mail_write),

    path('mail_view/<int:id>/', mail_view),
    path('mail_delete/<int:id>/', mail_dlt),
    path('web_mail_auth/<str:username>/<str:password>/', web_mail_auth),
    path('create_auth/', create_auth),
    path('update_auth/', update_auth)
]
