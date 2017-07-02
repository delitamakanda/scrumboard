from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from .serializers import ListSerializer, CardSerializer, UsersSerializer
from .models import Card, List
from django.contrib.auth.models import User
from mini_url.permissions import IsUserOfPost

class ListViewSet(ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = List.objects.all().filter(user=self.request.user)

        return queryset
        #user_id = self.request.user.id
        #queryset = List.objects.filter(user=user_id)

    #def get_permissions(self):
        #if self.request.method in permissions.SAFE_METHODS:
            #return (permissions.AllowAny(),)
        #return (permissions.IsAuthenticated(), IsUserOfPost(),)

def perform_create(self, serializer):
    instance = serializer.save(user=self.request.user)

    return super(ListViewSet, self).perform_create(serializer)



class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)



class UsersViewsSet(ModelViewSet):
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
