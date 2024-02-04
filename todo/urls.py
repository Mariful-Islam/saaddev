from django.urls import path
from todo.views import *

urlpatterns = [
    path('items/', getItems),
    path('item/<int:id>/', getItem),
    path('create/', createItem),
    path('update/<int:id>/', updateItem),
    path('delete/<int:id>/', deleteItem),
]
