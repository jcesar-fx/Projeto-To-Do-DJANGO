from django.urls import path
from . import views

urlpatterns = [
    path('helloWorld/', views.helloWorld),
    path('', views.tasklist, name='task-list'),
    path('yourname/<str:name>', views.yourname, name='your-name')
]