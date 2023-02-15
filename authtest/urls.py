from django.urls import path
from . import views
from .views import HomeView , UserCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('user_create/', UserCreateView.as_view(), name="user_create"),
]