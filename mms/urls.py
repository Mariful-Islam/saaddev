from django.urls import path
from .views import *


urlpatterns = [
    path('', router),
    path('students/', students),
    path('student/<str:username>/', student),
    path('floors/', floors),
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout),
    path('student_form/', student_form),

    path('room/<int:room_number>/', room),
    path('rooms/', rooms),
    path('payments/', payments),
    path('make_payment/', make_payment),
    path('payment_history/<str:username>/', payment_history),
    path('payment_confirmation/', payment_confirmation),
    path('leave_request/', leave_request),
    path('username_verification/<str:username>/', username_verification),
    path('edit_info/<str:username>/', edit_info)
]
