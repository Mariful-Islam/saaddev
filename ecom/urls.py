from django.urls import path
from ecom.views import *


urlpatterns = [
    path('', router),
    path('products/', products),
    path('product/<int:id>/', getProduct),
    path('total-cart/', total_cart),
    path('cart/<str:username>/', getCart),
    path('cart-item/<str:username>/<int:id>/', getCartItem),
    path('add-cart/<str:username>/<int:id>/', addToCart),
    path('item-increase/<int:id>/', addItemQuantity),
    path('item-decrease/<int:id>/', deleteItemQuantity),
    path('cart-delete/<int:id>/', deleteCartItem),
    path('cart_to_order/<str:username>/', cart_to_order),
    
    
    path('submit_delivery_place/', submit_delivery_place),
    path('get_delivery_place/<str:username>/', get_delivery_place),

    path('order_items/<str:username>/', order_items),

    path('signup/', signup),
    path('login/', login),
    path('user_info/<str:username>/', user_info),
    path('logout/', logout),

    # For admin url
    path('all_order_items/', all_order_items),
]
