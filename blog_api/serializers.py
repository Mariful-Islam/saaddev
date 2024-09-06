from rest_framework.serializers import ModelSerializer
from blog_api.models import *




class PostSerializer(ModelSerializer):
    class Meta :
        model = Post
        fields = [
            "id",
            "user",
            "username",
            "title",
            "description",
            "created",
            "updated",
            "tag",
            "views",
            "meta_title",
            "meta_description",
            "slug"
        ]

class CommentSerializer(ModelSerializer):
    class Meta :
        model = Comment
        fields = ["id",
                  "post",
                  "user",
                  "text",
                  "created",
                  "updated",
                  "post_id",
                  "post_title",
                    "username"
                  ]
