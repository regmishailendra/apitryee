from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from comments.models import Comments


class CommentListSerializer(ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id',
                  'content',
                  'time',
                  ]


