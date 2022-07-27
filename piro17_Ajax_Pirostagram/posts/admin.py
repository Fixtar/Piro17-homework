from django.contrib import admin
from .models import comment

# Register your models here.
@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    pass    