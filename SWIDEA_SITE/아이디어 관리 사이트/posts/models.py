from datetime import date
from operator import mod
from turtle import title
from django.db import models

# Create your models here.

class Devtool(models.Model):
    name = models.CharField(max_length=30,verbose_name='devtool name')
    kind = models.CharField(max_length=30,verbose_name='종류')
    content = models.TextField(verbose_name='content')

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    image = models.ImageField(blank = True, upload_to='posts/%Y%M%D',verbose_name='image')
    content = models.TextField(verbose_name='content')
    interest = models.IntegerField(default=0,verbose_name='관심도')
    devtool = models.ForeignKey(Devtool,on_delete = models.PROTECT,related_name='post_devtool')
    ideastar = models.BooleanField(default=False,verbose_name='아이디어스타')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')