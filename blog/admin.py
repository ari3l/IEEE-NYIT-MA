from django.contrib import admin
from .models import Event, Project, Post, User

# Register your models here.
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(User)

