from rest_framework.serializers import ModelSerializer
from .models import Post, Comment


# comments serializers
class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'name',
            'body',
            'creation_date',
        ]


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'name',
            'body',
        ]


class CommentDetailSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'name',
            'body',
            'creation_date',
            'change_date',
        ]


class CommentDeleteSerializer(ModelSerializer):
    class Meta:
        model = Comment


# posts serializers
class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'body',
            'creation_date',
        ]


class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'body',

        ]


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
        ]


class PostDetailSerializer(ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'body',
            'creation_date',
            'change_date',
            'comments',
        ]


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Post
