from django.urls import path 
from .views import ProfileView, UpdateProfile

urlpatterns = [
    path('<str:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', UpdateProfile.as_view(), name='update-profile'),
]