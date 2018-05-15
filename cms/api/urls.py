from django.conf.urls import url

from cms.api.views import PostListApiView, PostDetailApiView, PostDeleteApiView, PostUpdateApiView, \
    PostCreateApiView

app_name="postapiappname"

urlpatterns=[
    url(r'^(?P<pk>\d+)/$', PostDetailApiView.as_view(), name='detailstudent'),
    url(r'^create/$', PostCreateApiView.as_view(), name='createstudent'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateApiView.as_view(), name='editstudent'),
    url(r'^(?P<pk>\d+)/delete/$', PostDeleteApiView.as_view(), name='deletestudent'),
    url(r'^$', PostListApiView.as_view(), name='studentlist'),



]
