from django.db import models

from cms.models import PostModel


class Comments(models.Model):
    id=models.IntegerField
    content=models.CharField(max_length=20)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True,auto_now=False)


    def __str__(self):
        return self.content


















