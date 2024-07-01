from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user/', views.user_detail, name='detail'),
    path('user/edit/', views.user_edit, name='edit'),
    path('now_timezone', views.now_timezone, name='now_timezone'),
    path('now_datetime', views.now_datetime, name='now_datetime'),
]