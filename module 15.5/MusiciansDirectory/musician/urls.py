from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name="musician_list"),
    path('add/', views.add_musician, name="add_musician"),
    path('edit/<int:musician_id>/', views.edit_musician, name="edit_musician"),
]