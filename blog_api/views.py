from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog_api.models import *
from blog_api.serializers import *


# Create your views here.

@api_view(['GET'])
def home(request) :
    posts = Post.objects.all()
    serializers = PostSerializer(posts, many=True)
    return Response(serializers.data)


@api_view(['GET', 'POST'])
def create_post(request) :
    if request.method == "POST" :
        user = request.data["user"]
        title = request.data["title"]
        content = request.data["content"]
        tag = request.data["tag"]

        post = Post.objects.create(user=user, title=title, content=content, tag=tag)
        post.save()

        return Response("Post Created")

    return Response("")


@api_view(['GET'])
def post_view(request, id) :
    try :
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
    except :
        return Response("")


@api_view(['GET', 'DELETE'])
def post_delete(request, id) :
    try :
        post = Post.objects.get(id=id)
        post.delete()
        return Response("Deleted Successfully")
    except :
        return Response("")


@api_view(['GET'])
def user_post(request, user):
    posts = Post.objects.filter(user=user)
    serializers = PostSerializer(posts, many=True)
    return Response(serializers.data)


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


@api_view(['GET', 'DELETE'])
def delete_comment(request, id):
    try:
        comment = Comment.objects.get(id=id)
        comment.delete()
        return Response("Comment Deleted")
    except:
        return Response("")