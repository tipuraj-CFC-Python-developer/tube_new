from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),

   
    # API URLS
    path('profileapi/', profileAPI.as_view()),
    path('register/' , register.as_view()),
    path('login/' , login.as_view()),
    path('get_posts/', views.get_posts, name='get_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('get_followers/', views.get_followers, name='get_followers'),
    path('create_follower/', views.create_follower, name='create_follower'),
    
    path('logoutapi/', views.logout_api, name='logout'),
    
    
]
