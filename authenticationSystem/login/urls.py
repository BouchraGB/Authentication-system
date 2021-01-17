from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
    path('registerPage/', views.registerPage, name='registerPage'),
    path('registerPage/register/', views.register, name='register'),
] 
