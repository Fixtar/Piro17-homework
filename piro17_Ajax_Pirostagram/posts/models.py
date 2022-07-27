from django.db import models

# Create your models here.
class comment(models.Model):
    content = models.TextField()
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)