from rest_framework.generics import CreateAPIView, ListAPIView

from comments.api.serializers import CommentListSerializer
from comments.models import Comments


class CommentsList(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



