from django.urls import path
from enlaces import views

urlpatterns = [
    path('', views.index, name='index'),
    path('link/create/', views.LinkCreate.as_view(), name='link_create'),
    path('link/<int:pk>/update/', views.LinkUpdate.as_view(), name='link_update'),
    path('delete/<int:pk>/delete/', views.LinkDelete.as_view(), name='link_delete'),    
]
