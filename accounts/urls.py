from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('user/<uuid:user_id>', views.user_detail, name='user_detail'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uuid:user_id>/', views.activate, name='activate'),
    path('password_change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('profile/', views.profile, name='users-profile'),
    path('change_email', views.change_email, name='change_email'),
    path('change_email_done/<str:old_email>/<str:new_email>/', views.change_email_done, name='change_email_done' )
    ]