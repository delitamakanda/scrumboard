# http://djangofeeds.soup.io/since/604909962?newer=1
import json, requests, random, re

from pprint import pprint
from django.views import generic
from django.http.response import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, mail_admins #send_email
from django.template import Context
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.template.loader import get_template #send a .txt template
from django.contrib import messages
import datetime
from django.contrib.auth import login
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import MiniUrl, Profile
from .forms import MiniUrlForm, SignupForm, UserProfileForm
from mini_url.tokens import account_activation_token
from django.core.mail import send_mail

verify_token = "tes_un_pd_si_tu_mets_pas_de_texte"


def get_joke(fbid, recevied_message):
    joke_text = requests.get("http://api.icndb.com/jokes/random/").json()['value']['joke']
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%'EAABcBLigDYcBAIzoAv6dgCR1RHJ0jfEMKepWToFEhmdYwbIifW9JjsAcEMRPGiQsO3gRPLZBBDDFtlFUExtX9BZAaJZBCZAxW7wZBqPZCZCSjMScab9k3zQjNZAKagEecOvQ061qz2mQgdOliZBXhe3WSUc6PEulBpyGWIvSymoa8VQZDZD'
    response_msg = json.dumps({"recipient": {"id": fbid }, "message": {"text": joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())

class jokebot(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == verify_token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    get_joke(message['sender']['id'], message['message']['text'])
                else:
                    HttpResponse('a jerk has posted a sticker')
        return HttpResponse()

def liste(request):
    minis_list = MiniUrl.objects.order_by('-nb_acces')
    page = request.GET.get('page', 1)
    max_count = minis_list.count()

    paginator = Paginator(minis_list, 15)
    try:
        minis = paginator.page(page)
    except PageNotAnInteger:
        minis = paginator.page(1)
    except EmptyPage:
        minis = paginator.page(paginator.num_pages)

    return render(request, 'mini_url/liste.html', locals()) #built-in function for avoid writing variables in context


def success_miniurl(request, pk):
    mini = get_object_or_404(MiniUrl, pk=pk)
    send_mail('New url submitted', 'a new url was submitted.', 'from@shorten.com', ['delita.makanda@gmail.com'], fail_silently=False)
    return render(request, 'mini_url/success.html', {'mini': mini})

def nouveau(request):
    if request.method == 'POST':
        form = MiniUrlForm(request.POST)
        if form.is_valid():
            mini = form.save(commit=False)
            mini.date = timezone.now()
            form.save()
            return redirect('success_miniurl', pk=mini.pk)
    else:
        form = MiniUrlForm()
    return render(request, 'mini_url/nouveau.html', {'form' : form})

def redirection(request, code):
    mini = get_object_or_404(MiniUrl, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            #user.refresh_from_db()
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            current_site = get_current_site(request)
            subject = 'Activer votre compte'
            message = render_to_string('mini_url/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return redirect('liste')
            return redirect('account_activation_sent')
    else:
        form = SignupForm()
    return render(request, 'mini_url/signup.html', {'form': form})




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('liste')
    else:
        return render(request, 'mini_url/account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'mini_url/account_activation_sent.html')


class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field = "username"
	template_name = "mini_url/user_detail.html"

	def get_object(self, queryset=None):
		user = super(UserProfileDetailView, self).get_object(queryset)
		UserProfile.objects.get_or_create(user=user)
		return user

class UserProfileEditView(UpdateView):
	model = Profile
	form_class = UserProfileForm
	template_name = "mini_url/edit_profile.html"
	success_message = "%(user)s was updated successfully"

	def get_object(self, queryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse('profile', kwargs={'slug': self.request.user})

