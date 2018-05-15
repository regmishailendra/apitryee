from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from cms.api.permission import IsOwnerOrReadOnly
from cms.api.serializers import PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer
from cms.models import PostModel


class PostListApiView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']  # also can do this  lets to do ?search=    as our ?q=    ..&ordering=title  if put -title it will reverse

    def get_queryset(self):
        queryset_list = PostModel.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query))
            return queryset_list
        return queryset_list


class PostCreateApiView(CreateAPIView):
    #queryset = PostModel.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailApiView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializer


class PostUpdateApiView(RetrieveUpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteApiView(DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializer
