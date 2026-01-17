from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('flag/<int:message_id>/', views.flag_message, name='flag_message')
]
