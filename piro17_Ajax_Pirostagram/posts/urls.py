from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/', views.delete, name='delete'),
    path('like/', views.like, name='like'),
]

app_name = "posts"