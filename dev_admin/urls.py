from django.urls import path
from .views import *



urlpatterns = [
    path('saaddev_tables/', SaadDevTables.as_view()),
    path('services/', Services.as_view()),
    path('service/<int:pk>/', Service.as_view()),
    path('projects/', Projects.as_view()),
    path('project/<int:pk>/', Project.as_view()),
    path('ecom_tables/', EcomTables.as_view()),
]
