from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewgallery, name='gallery'),
    path('photo/<int:pk>/', views.viewphoto, name='photo'),
    path('add', views.addphoto, name='add'),
]
  