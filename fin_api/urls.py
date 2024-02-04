from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRouter),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),\
    path('transfer/', views.transfer),
    path('transaction/<str:username>/', views.transaction),
    path('ledger/', views.ledger),
    path('balance/<str:username>/', views.balance),

    path('friends/', views.friends),
    path('all_user/', views.all_user),
    
    path('create_bank_account/', views.create_bank_account),
    path('get_bank_account/<str:username>/', views.get_bank_account),
    path('find_bank_account/<int:id>/', views.find_bank_account),
    path('verify_bank_account/<int:id>/', views.verify_bank_account),

    path('user_info/<str:username>/', views.user_info),
    
    path('create-profile/', views.create_profile),
    path('profile/<str:username>/', views.get_profile),

    path('revenue/', views.revenue),
    path('create_gas_fee/', views.create_gas_fee),
    path('update_gas_fee/', views.update_gas_fee),
]
