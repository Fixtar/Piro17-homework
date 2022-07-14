from turtle import title
from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    openyear = models.IntegerField(verbose_name="Open Year")
    genre= models.CharField(max_length=100, verbose_name="Genre")
    starpoint = models.IntegerField(verbose_name="Star Point")
    director = models.CharField(max_length=100, verbose_name="Director")
    actor = models.CharField(max_length=100, verbose_name="Actor")
    runningtime = models.IntegerField(verbose_name="Running Time")
    review = models.TextField(verbose_name="Review")