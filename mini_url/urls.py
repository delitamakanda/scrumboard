from django.conf.urls import url
from . import views
from mini_url.views import jokebot
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from mini_url.sitemap import (
    MiniUrlSitemap,
)

sitemaps = {
    'urls': MiniUrlSitemap,
}

# < 1.9
#urlpatterns = ('mini_url.views',
#    url(r'^$', 'liste', name='url_liste'),
#    url(r'^nouveau/$', 'nouveau', name='url_nouveau'),
#    url(r'^(?P<code>\w{6})/$', 'redirection', name='url_redirection')
#)
#url(r'^$', views.post_list, name='post_list'),
#url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
#url(r'^post/new/$', views.post_new, name='post_new'),
#url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
#url(r'^login/$', views.login_view, name="login"),
#url(r'^logout/$', views.logout_view, name="logout"),

urlpatterns = [
    url(r'^urls/$', views.liste, name='liste'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^$', views.nouveau, name='nouveau'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='redirection'),
    url(r'^urls/success/(?P<pk>\d+)/$', views.success_miniurl, name='success_miniurl'),
    url(r'^privacy-policies/$', TemplateView.as_view(template_name='mini_url/privacy-policies.html'), name="privacy-policies"),
    url(r'^donut/?$', jokebot.as_view(), name='donut_bot'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
