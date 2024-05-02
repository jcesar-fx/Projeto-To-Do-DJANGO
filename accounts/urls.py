from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup'),
   
]