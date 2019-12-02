from django.urls import path
from enlaces import views

urlpatterns = [
    path('', views.index, name='index'),
]
