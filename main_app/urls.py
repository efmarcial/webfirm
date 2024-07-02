from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='Home'),
    path('register/', views.register, name="Register"),
    path('account/', views.account, name="Account"),
    path('login/', views.login_page, name="Login Page"),
    path('custom_web/', views.custom_web, name='Custom Web'),
    path('seo/', views.seo, name='SEO'),
    path('hosting/', views.hosting, name="Hosting"),
    path('marketing/', views.marketing, name="Marketing"),
    path('services/', views.services, name="Services"),
    path('articles/', views.article, name="Articles"),
    path('about/', views.about, name="About"),
    path('blog/', views.blog, name='Blog'),
    path('results/', views.results, name='Results'),
    path('contact/', views.contact, name='Contact'),
]
