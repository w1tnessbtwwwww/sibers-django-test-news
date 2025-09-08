# newspaper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('add/', views.add_news, name='add_news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]