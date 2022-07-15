from turtle import title
from django.db import models

# Create your models here.
class Review(models.Model):
    genrecategory=(('Action','Action'),('Adventure','Adventure'),('Animation','Animation'),('Comedy','Comedy'),('Crime','Crime'),('Documentary','Documentary'),('Drama','Drama'),('Family','Family'),('Fantasy','Fantasy'),('History','History'),('Horror','Horror'),('Music','Music'),('Mystery','Mystery'),('Romance','Romance'),('Science Fiction','Science Fiction'),('TV Movie','TV Movie'),('Thriller','Thriller'),('War','War'),('Western','Western'))
    title = models.CharField(max_length=100, verbose_name="Title")
    openyear = models.IntegerField(verbose_name="Open Year")
    genre= models.CharField(max_length=100, choices=genrecategory)
    starpoint = models.IntegerField(verbose_name="Star Point")
    director = models.CharField(max_length=100, verbose_name="Director")
    actor = models.CharField(max_length=100, verbose_name="Actor")
    runningtime = models.IntegerField(verbose_name="Running Time")
    review = models.TextField(verbose_name="Review")