from django.conf.urls import url
from . import views
from mini_url.views import jokebot
from django.views.generic.base import TemplateView
from django.conf import settings


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^privacy-policies/$', TemplateView.as_view(template_name='mini_url/privacy-policies.html'), name="privacy-policies"),
    url(r'^donut/?$', jokebot.as_view(), name='donut_bot'),
]
