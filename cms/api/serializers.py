from rest_framework.fields import SerializerMethodField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from cms.models import PostModel


class PostListSerializer(ModelSerializer):
    detail = HyperlinkedIdentityField(
        lookup_field='pk',
        view_name='postapi:detailstudent'
    )
    user = SerializerMethodField()    #for getting username instead of the id we had shown
    #image=SerializerMethodField()

    class Meta:
        model = PostModel
        fields = [
            'title',
            'content',
            'pk',
            'detail',
            'createdDate',
            'user',
            'image',
            # 'edit_url',
        ]
    def get_user(self,obj):
        return obj.user.username


    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image=None

        return request.build_absolute_uri(obj.image)

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = [
            'title',
            'content',
        ]


class PostDetailSerializer(ModelSerializer):
    edit_url = HyperlinkedIdentityField(
        lookup_field='pk',
        view_name='postapi:editstudent'
    )

    class Meta:
        model = PostModel
        fields = [
            'title',
            'content',
            'pk',
            'edit_url',
            'createdDate',
            'user',

        ]
