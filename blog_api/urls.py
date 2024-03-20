from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', Posts.as_view()),
    path('create_post/', create_post),
    path('post/<int:id>/', post_view),
    path('user_post/<str:user>/', user_post),
    path('post_delete/<int:id>/', post_delete),
    path('post_comment/', post_comment),
    path('comment/<int:id>/', comment),
    path('user_comment/<str:user>/', user_comment),
    path('comment_post/<str:comment>/', comment_post),
    path('delete_comment/<int:id>/', delete_comment),
]