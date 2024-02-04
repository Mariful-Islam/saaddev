from rest_framework import serializers
from base.models import Service, Project, ProjectStatstic, Partnership, Client, Contact, WebMail


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", 
                  "name", 
                  "github", 
                  "link", 
                  "image", 
                  "stack", 
                  "requirement", 
                  "description",
                  "get_stack_list"
        ]


class ProjectStatsticSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatstic
        fields = ["id", "get_project_name", "get_status", "get_project_link"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", 
                  "username", 
                  "email", 
                  "subject", 
                  "message", 
                  "time",
                  "category",
                  "get_date", 
                  "get_time", 
                  "get_category"
                  ]


class WebMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebMail
        fields = "__all__"