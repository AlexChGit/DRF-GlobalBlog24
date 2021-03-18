from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
    CommentDeleteAPIView,
)

urlpatterns = [
    path("posts", PostListAPIView.as_view(), name="posts"),
    path("post/<int:pk>", PostDetailAPIView.as_view(), name="post"),
    path("post/create", PostCreateAPIView.as_view(), name="post-create"),
    path("post/update/<int:pk>", PostUpdateAPIView.as_view(), name="post-update"),
    path("post/delete/<int:pk>", PostDeleteAPIView.as_view(), name="post-delete"),
    path("comments", CommentListAPIView.as_view(), name="comments"),
    path("comment/<int:pk>", CommentDetailAPIView.as_view(), name="comment"),
    path("comment/create", CommentCreateAPIView.as_view(), name="comment-create"),
    path("comment/delete/<int:pk>", CommentDeleteAPIView.as_view(), name="comment-delete"),
]
