from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout),
    path('token-verify/', token_verify),
    path('get-user/<str:username>/', get_user)
]