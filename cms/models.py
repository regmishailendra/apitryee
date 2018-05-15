from django.contrib.auth.models import User
from django.db import models


class PostModel(models.Model):
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120)
    user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    createdDate=models.DateTimeField(auto_now_add=False,auto_now=True)
    image=models.ImageField(null=True)

    def __str__(self):
        return  self.title


