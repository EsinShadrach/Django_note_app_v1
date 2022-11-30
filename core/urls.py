from django.urls import path
from .import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.homepage, name='home'),
    # path('notes/', views.homepage, name='home'),
    path('notes/<str:pk>/', views.detailed, name='detailed'),
    path('create-note/', views.create, name='create'),
]
