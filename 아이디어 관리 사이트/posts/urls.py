from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "posts"

urlpatterns = [
    path('',views.home,name='home'),
    path('create/', views.create, name='create'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('devtools/',views.devtool,name='devtoolshome'),
    path('devtools/create/', views.devtoolcreate, name='devtoolscreate'),
    path('devtools/detail/<int:id>/', views.devtooldetail, name='devtoolsdetail'),
    path('devtools/update/<int:id>/', views.devtoolupdate, name='devtoolsupdate'),
    path('devtools/delete/<int:id>/', views.devtooldelete, name='devtoolsdelete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)