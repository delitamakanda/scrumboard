from django.conf.urls import url
from . import views
from mini_url.views import jokebot, UserProfileDetailView, UserProfileEditView
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required as auth
from django.conf import settings


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'mini_url/registration/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'mini_url/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'mini_url/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,  {'template_name': 'mini_url/registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^$', auth_views.login, {'template_name': 'mini_url/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'mini_url/registration/logged_out.html'}, name='logout'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^user/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name='profile'),
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name='edit_profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^privacy-policies/$', TemplateView.as_view(template_name='mini_url/privacy-policies.html'), name="privacy-policies"),
    url(r'^donut/?$', jokebot.as_view(), name='donut_bot'),
]
