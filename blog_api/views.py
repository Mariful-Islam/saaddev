from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from blog_api.models import *
from blog_api.serializers import *


# Create your views here.


class Posts(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        username = request.data["username"]
        title = request.data["title"]
        description = request.data["description"]
        tag = request.data["tag"]
        meta_title = request.data["meta_title"]
        meta_description = request.data["meta_description"]
        slug = request.data["slug"]

        user = User.objects.get(username=username)

        post = Post.objects.create(
            user=user,
            title=title,
            description=description,
            tag=tag,
            meta_title=meta_title,
            meta_description=meta_description,
            slug=slug
        )
        post.save()
        return post


@api_view(['GET', 'POST'])
def create_post(request) :
    if request.method == "POST" :
        username = request.data["username"]
        title = request.data["title"]
        content = request.data["content"]
        tag = request.data["tag"]

        user = User.objects.get(username=username)

        if username and title and content and tag:
            post = Post.objects.create(user=user, title=title, content=content, tag=tag)
            post.save()
            return Response("Post Created")
        else:
            return Response("Form is Blank")
    return Response("")


class PostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    

@api_view(['GET'])
def user_post(request, username):
    try:
        posts = Post.objects.filter(user = username)
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)
    except:
        return Response("No post found", status=status.HTTP_404_NOT_FOUND)


class Comments(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        post_slug = request.data['slug']
        username = request.data['username']
        text = request.data['text']
        
        post = Post.objects.get(slug=post_slug)
        user = User.objects.get(username=username)

        comment = Comment.objects.create(post=post, user=user, text=text)
        serializer = self.get_serializer(comment)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'


@api_view(['GET'])
def post_comment(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    try:
        comment = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    except:
        return Response("No comments", status=status.HTTP_404_NOT_FOUND)


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

