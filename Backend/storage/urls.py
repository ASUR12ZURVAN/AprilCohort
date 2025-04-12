from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.create_user),
    path('api/users/<int:pk>/', views.delete_user),

    path('api/calls/', views.create_call),
    path('api/calls/<int:pk>/', views.delete_call),

    path('api/tickets/', views.create_ticket),
    path('api/tickets/<int:pk>/', views.delete_ticket),

    path('api/leads/', views.create_lead),
    path('api/leads/<int:pk>/', views.delete_lead),
]
