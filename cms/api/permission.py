from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message= 'You must be the owner of this object.'




    def has_object_permission(self, request, view, obj):

        #member=Membership.objects.get(user=request.user_
        #member.is_active   we can do this too for more powerful permission as we want

        # my_safe_method=['PUT']
        # if(request.method in my_safe_method):
          return obj.user == request.user
