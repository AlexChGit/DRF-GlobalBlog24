from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path("users", UserProfileListCreateView.as_view(), name="users"),
    path("user/<int:pk>", UserProfileDetailView.as_view(), name="user"),
]
