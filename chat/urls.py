from django.urls import path
from django.contrib.auth import views as auth_views # Import important
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('registration/login/', views.room_detail, name='room_detail'),
    path('send/', views.send_message, name='send_message'),
    path('room/<slug:slug>/', views.room_detail, name='room_detail'),
    path('flag/<int:message_id>/', views.flag_message, name='flag_message'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('get_messages/<int:room_id>/', views.get_messages, name='get_messages'),
]