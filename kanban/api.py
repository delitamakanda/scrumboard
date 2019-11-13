from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import permissions, generics, status
from django.contrib.messages import add_message
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from django.http import Http404
from django.utils.translation import gettext as _

from .serializers import ListSerializer, CardSerializer, UsersSerializer, TodoSerializer
from .models import Card, List, Todo
from django.contrib.auth.models import User
from .permissions import IsUserOfPost, IsAdminUser, IsAdminOrReadOnly

import stored_messages

class ListViewSet(ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = [ permissions.IsAuthenticated, ]

    def get_queryset(self):
        queryset = List.objects.all().filter(user=self.request.user)

        return queryset


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ListViewSet, self).dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        add_message(self.request._request, stored_messages.STORED_INFO, _(' %s created a list') % self.request.user)
        return super(ListViewSet, self).perform_create(serializer)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [ permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        add_message(self.request._request, stored_messages.STORED_INFO, _('%s created a card') % self.request.user)
        return super(CardViewSet, self).perform_create(serializer)


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [ permissions.IsAuthenticated ]

    def get_queryset(self):
        queryset = Todo.objects.all().filter(user=self.request.user)

        return queryset

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TodoViewSet, self).dispatch(request, *args, **kwargs)


    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        add_message(self.request._request, stored_messages.STORED_INFO, _('%s created a to do') % self.request.user)
        return super(TodoViewSet, self).perform_create(serializer)


class UsersViewsSet(ModelViewSet):
    serializer_class = UsersSerializer
    permission_classes = [ permissions.IsAuthenticated, ]
    queryset = User.objects.all()
