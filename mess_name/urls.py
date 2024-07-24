from django.urls import path
from .views import *


urlpatterns = [
    path('setup/', welcome),
    path('admin_login/', admin_login),
    path('get_admin/', get_admin),
    path('get_mess/<str:username>/', get_mess),
    path('get_messes/', get_messes),
    path('get_all_admin/', get_all_admin)
]