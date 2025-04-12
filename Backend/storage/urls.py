from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.create_user, name='create_user'),
    path('user/delete/<int:pk>/', views.delete_user, name='delete_user'),
    path('call/create/', views.create_call, name='create_call'),
    path('call/delete/<int:pk>/', views.delete_call, name='delete_call'),
]
