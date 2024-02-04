
from django.urls import path
from . import views

from django.conf import settings
from django.urls import re_path as url
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('service/', views.service, name="service"),
    path('service/<str:service_name>/',
         views.single_service, name="single-service"),
    path('project/', views.project, name="project"),
    path('project/<str:project_name>/',
         views.single_project, name="single-project"),
    path('client/', views.client, name="client"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('mail/', views.mail, name="mail"),
    path('mail-view/<int:id>/', views.mail_view, name="mail-view"),
    path('mail-delete/<int:id>/', views.mail_delete, name='mail-delete'),
    path('mail_compose/', views.mail_compose, name="mail-compose"),

    url(r'^download/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
