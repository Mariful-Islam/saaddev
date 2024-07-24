from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', Posts.as_view()),
    path('create_post/', create_post),
    path('user_post/<str:username>/', user_post),
    path('post/<int:id>/', PostView.as_view()),
    path('post_comment/', post_comment),
    path('comment/<int:id>/', comment),
    path('comment_view/<int:pk>/', CommentView.as_view()),
    path('user_comment/<str:user>/', user_comment),
    path('comment_post/<str:comment>/', comment_post)
]