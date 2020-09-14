from django.contrib import admin
from .models import Project,Subscriber,Client,Hire

# Register your models here.
admin.site.register(Project)
admin.site.register(Subscriber)
admin.site.register(Client)
admin.site.register(Hire)
