from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('login/', views.loginpage, name='login'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutpage, name='logout'),
]