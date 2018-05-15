from django.conf.urls import url
from comments.api.views import CommentsList

urlpatterns = [
    url(r'^$', CommentsList.as_view(), name='commentslist'),



]




