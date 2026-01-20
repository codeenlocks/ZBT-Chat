"""
URL configuration for zbt_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create-room/', views.create_room, name='create_room'),
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('delete-room/<slug:slug>/', views.delete_room, name='delete_room'),
    path('flag/<int:message_id>/', views.flag_message, name='flag_message'),
    path('', views.index, name='index'),
    path('', include('chat.urls')),
]