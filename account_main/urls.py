from django.contrib import admin
from django.urls import path, include
from account_main import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('set_user_data/', views.set_user_data, name="set_user_data"),
    path('login/', views.login, name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('login1/', views.LoginView.as_view(), name="login1"),
]
