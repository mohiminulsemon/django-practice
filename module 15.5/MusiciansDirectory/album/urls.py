from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name="album_list"),
    path('add/', views.add_album, name="add_album"),
    path('edit/<int:album_id>/', views.edit_album, name="edit_album"),
    path('delete/<int:album_id>/', views.delete_album, name="delete_album"),
]