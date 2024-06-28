from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='Home'),
    path('register/', views.register, name="Register"),
    path('account/', views.account, name="Account"),
    path('login/', views.login_page, name="Login Page"),
    
]
