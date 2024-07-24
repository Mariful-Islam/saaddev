from django.urls import path
from .views import *


urlpatterns = [
    path('', router),
    path('total_students/', total_students),
    path('students/<str:mess>/', students),
    path('student/<str:username>/', student),
    path('student_form/<str:username>/', student_form),

    path('room/<str:room_number>/', room),
    path('rooms/<str:mess>/', rooms),
    path('payments/<str:mess>/', payments),
    path('make_payment/', make_payment),
    path('payment_history/<str:username>/', payment_history),
    path('payment_confirmation/<str:mess>/', payment_confirmation),
    path('leave_request/<str:username>/', leave_request),
    path('edit_info/<str:username>/', edit_info)
]
