from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.AccountHome, name='account_home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),

]