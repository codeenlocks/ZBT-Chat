from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('send/', views.send_message, name='send_message'),
    # Nouvelle route pour accéder à un salon spécifique :
    path('room/<slug:slug>/', views.room_detail, name='room_detail'),
]