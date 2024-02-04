from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='fin-home'),
    path('transaction/', views.transaction, name='transaction'),
    path('ledger/', views.ledger, name='ledger'),

    path('transfer/', views.transfer, name='transfer'),
    path('transfer/<str:account_id>/',
         views.friend_transfer, name='friend_transfer'),
    path('balance/<str:username>/', views.balance, name='balance'),
    path('friends/', views.friends, name='friends'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.log_out, name='logout'),
    path('bank-account/', views.bank_account, name='bank-account'),
    path('setting/', views.setting, name='setting'),
    path('edit-user/<str:username>/', views.edit_user, name='edit-user'),
    path('add-profile/',
         views.add_profile, name='add-profile'),
    path('edit-profile/<str:username>/',
         views.edit_profile, name='edit-profile'),
    path('developer/', views.developer, name='developer'),
    path('update-gas-fee/', views.gas_fee_update, name='update-gas-fee')
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
