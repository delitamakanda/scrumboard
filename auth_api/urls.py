from django.conf.urls import url

from .api import LoginView, LogoutView, SignupView

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^register/$', SignupView.as_view()),
]
