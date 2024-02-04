from django.contrib import admin
from .models import Service, Project, ProjectStatstic, Client, Partnership, Contact, WebMail

# Register your models here.

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ProjectStatstic)
admin.site.register(Client)
admin.site.register(Partnership)
admin.site.register(Contact)

admin.site.register(WebMail)

