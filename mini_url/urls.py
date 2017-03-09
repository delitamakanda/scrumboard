from django.conf.urls import url
from . import views

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
    url(r'^$', views.liste, name='liste'),
    url(r'^nouveau/$', views.nouveau, name='nouveau'),
    url(r'^(?P<code>\w{6})/$', views.redirection, name='redirection'),
]
