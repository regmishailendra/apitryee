from django.contrib import admin

# Register your models here.
from cms.models import PostModel


class PostModelAdmin(admin.ModelAdmin):
     list_display = ('title','content')



admin.site.register(PostModel, PostModelAdmin)













