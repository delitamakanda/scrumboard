from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions, generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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

    #def get_permissions(self):
        #if self.request.method in permissions.SAFE_METHODS:
            #return (permissions.AllowAny(),)
        #return (permissions.IsAuthenticated(), IsUserOfPost(),)
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListViewSet, self).dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        return super(ListViewSet, self).perform_create(serializer)
    
    def delete(self):
        pass



class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)



class UsersViewsSet(ModelViewSet):
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
