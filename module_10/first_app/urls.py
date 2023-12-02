
from django.urls import path
# from first_app.views import home ( method 1)
# from first_app import views  (method 2)
from . import views

urlpatterns = [
  
    path('',views.home),
]
