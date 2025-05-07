from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_list, name='media-list'),
    path('add/', views.add_media_item, name='media-add'),
    path('edit/<int:pk>/', views.edit_media_item, name='media-edit'),
    path('delete/<int:pk>/', views.delete_media_item, name='media-delete'),
]
