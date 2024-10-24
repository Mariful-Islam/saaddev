from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from blog_api.models import *
from blog_api.serializers import *


# Create your views here.

class UserList(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = User.objects.filter(product='blog')
        return users

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


class PostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    # def update(self, request, *args, **kwargs):
    #     post_slug = self.kwargs.get(self.lookup_field)
    #     post = Post.objects.get(slug=post_slug)

    #     username = request.data['username']
    #     title = request.data["title"]
    #     description = request.data["description"]
    #     tag = request.data["tag"]

    #     meta_title = request.data['meta_title']
    #     meta_description = request.data['meta_description']
    #     slug = request.data['slug']

    #     user = User.objects.get(username=username)

    #     post.user = user
    #     post.title = title
    #     post.description = description
    #     post.tag = tag
    #     post.meta_title = meta_title
    #     post.meta_description = meta_description



    #     return 


    

@api_view(['GET'])
def user_post(request, username):
    try:
        user = User.objects.get(username=username)
        posts = Post.objects.filter(user = user)
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
        
        try:
            post = Post.objects.get(slug=post_slug)
            user = User.objects.get(username=username)

            if len(text) > 0:
                comment = Comment.objects.create(post=post, user=user, text=text)
                serializer = self.get_serializer(comment)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'data': 'Comment is empty'}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'data': 'Error create post.'}, status=status.HTTP_400_BAD_REQUEST)
    

class CommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        id = self.kwargs.get(self.lookup_field)
        post_slug = request.data['post_slug']
        username = request.data['username']
        text = request.data['text']

        try:
            post = Post.objects.get(slug=post_slug)
            user = User.objects.get(username=username)

            comment = Comment.objects.get(id=id)
            comment.post = post
            comment.user = user
            comment.text = text
            comment.save()
            return Response({'data': 'Comment Updated.'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'data': 'Error Update Comment.'}, status=status.HTTP_400_BAD_REQUEST)


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




class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()