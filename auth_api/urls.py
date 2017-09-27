from django.conf.urls import url

from .api import LoginView, LogoutView, SignupView, CheckoutUser

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register/$', SignupView.as_view()),
    url(r'^check_login/$', CheckoutUser.as_view()),
]
