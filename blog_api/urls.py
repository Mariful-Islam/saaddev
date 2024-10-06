from django.urls import path
from .views import *

urlpatterns = [
    path('user-list/', UserList.as_view()),
    path('posts/', Posts.as_view()),
    path('user_post/<str:username>/', user_post),
    path('post/<str:slug>/', PostView.as_view()),

    path('post_comment/', post_comment),
    path('comments/', Comments.as_view()),
    path('post-comments/<str:post_slug>/', post_comment),

    path('comment-view/<str:id>/', CommentView.as_view()),

    path('user_comment/<str:user>/', user_comment),
    path('comment_post/<str:comment>/', comment_post),
    
    path('category-list/', CategoryView.as_view(), name='category-list')
]