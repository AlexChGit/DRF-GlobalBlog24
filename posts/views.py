from accounts.permissions import IsOwnerProfileOrReadOnly
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import (
    Post,
    Comment,
)
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostUpdateSerializer,
    PostDeleteSerializer,
    CommentListSerializer,
    CommentDetailSerializer,
    CommentCreateSerializer,
    CommentDeleteSerializer,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
)


# Create your views here.

# posts views
class PostListAPIView(ListAPIView):
    queryset = Post.objects.filter(visible=True)
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        self.check_object_permissions(self.request, obj)
        obj.visible = False
        return obj


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    permission_classes = [IsAdminUser]


# comments views
class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.filter(visible='1')
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [AllowAny]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer
    permission_classes = [IsAdminUser]
