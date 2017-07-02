"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import ensure_csrf_cookie
from mini_url.views import jokebot, UserProfileDetailView, UserProfileEditView, signup, account_activation_sent, activate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required as auth
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scrumboard/', include('mini_url.urls')),
    url(r'^auth_api/', include('auth_api.urls')),
    url(r'^$', ensure_csrf_cookie(TemplateView.as_view(template_name='index.html'))),
    url(r'^signup/$', signup, name='signup'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'mini_url/registration/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'mini_url/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'mini_url/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,  {'template_name': 'mini_url/registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^user/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name='profile'),
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name='edit_profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
    url(r'^donut/?$', jokebot.as_view(), name='donut_bot'),
]
