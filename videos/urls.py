from django.contrib import admin
from django.urls import path
from .views import CreateVideo, DetailVideo, UpdateVideo, DeleteVideo, VideoCategoryList, SearchVideo, send_email, success_view, login_view

urlpatterns = [
    path('create/', CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='video-delete'),
    path('category/<int:pk>', VideoCategoryList.as_view(), name='category-list'),
    path('search/', SearchVideo.as_view(), name='video-search'),
    path('send/', send_email, name='send_email'),
    path('success/', success_view, name='success'),
    path('login/', login_view ,name='login')
]