from django.contrib import admin
from .models import Devtool, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Devtool)
class PostAdmin(admin.ModelAdmin):
    pass