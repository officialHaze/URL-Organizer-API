from django.urls import path
from . import views

urlpatterns = [
    path('organize-url/', views.organize_urls, name="URLs' Organizer")
]

