from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', ChatListView.as_view(), name='chat-home'),
    path('post/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),
    path('post/new/', ChatCreateView.as_view(), name='chat-create'),
    path('post/<int:pk>/update/', ChatUpdateView.as_view(), name='chat-update'),
    path('post/<int:pk>/delete/', ChatDeleteView.as_view(), name='chat-delete'),
    path('about/', views.about_page, name='chat-about'),
    path('favicon.ico', views.favicon, name='favicon'),
]
