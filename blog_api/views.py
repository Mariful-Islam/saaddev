from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from blog_api.models import *
from blog_api.serializers import *


# Create your views here.


class Posts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET', 'POST'])
def create_post(request) :
    if request.method == "POST" :
        user = request.data["user"]
        title = request.data["title"]
        content = request.data["content"]
        tag = request.data["tag"]

        if user and title and content and tag:
            post = Post.objects.create(user=user, title=title, content=content, tag=tag)
            post.save()
            return Response("Post Created")
        else:
            return Response("Form is Blank")
    return Response("")


class PostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

@api_view(['GET'])
def user_post(request, username):
    try:
        posts = Post.objects.filter(user = username)
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)
    except:
        return Response("No post found", status=status.HTTP_404_NOT_FOUND)



@api_view(['GET', 'POST'])
def post_comment(request) :
    if request.method == "POST" :
        post_id = request.data["post_id"]
        user = request.data["user"]
        text = request.data["text"]

        comment = Comment.objects.create(post_id=post_id, user=user, text=text)
        comment.save()

        return Response("You comment on a post..")

    return Response("")


@api_view(['GET'])
def comment(request, id):
    comment = Comment.objects.filter(post_id=id)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)

class CommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def user_comment(request, user):

    comments = Comment.objects.filter(user=user)

    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_post(request, comment):
    post = Post.objects.get(comment__text=comment)
    serializer = PostSerializer(post)
    return Response(serializer.data)

