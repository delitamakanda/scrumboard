from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from rest_framework import status, views, permissions
from rest_framework.response import Response
from django.shortcuts import HttpResponse
import json

from .serializers import UserSerializer

class SignupView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class LoginView(views.APIView):

    @method_decorator(csrf_protect)
    def post(self, request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"))

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'User or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response(UserSerializer(user).data)


class LogoutView(views.APIView):

    """docstring for LogoutView."""
    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_200_OK)



class CheckoutUser(views.APIView):
    
    def check_login(request):
        if request.user.is_authenticated():
            return HttpResponse(json.dumps({'result': {'logged': True}, 'user': request.user.username }), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'result': {'logged': False}}), content_type="application/json")
        
        

class GetCurrentUser(views.APIView):
    
    def get(request):
        pass
