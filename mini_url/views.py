import json, requests, random, re

from pprint import pprint
from django.views import generic
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import MiniUrl
from .forms import MiniUrlForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, mail_admins#, send_email
from django.template import Context
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.loader import get_template #send a .txt template
from django.contrib import messages
import datetime
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

verify_token = "my_voice_is_my_password"


def get_joke(fbid, recevied_message):
    joke_text = requests.get("http://api.icndb.com/jokes/random/").json()['value']['joke']
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%'EAAYhpiOyWHsBAGXoYf6H6OigfpnPuZBwtGVQEoEGucqZA2ZBlRAPTfJ3KYGqaZBlhh82oV7jQgLkXPUZAGqFS9d0FfW5X0Wkbj6ZCFuo4sa8FmQZBZBPMXAZCaqgracbeHFNxk2vOBKlfN2mvUxc7hk6plLZBxuFVUxCZAE4BW8qOGYVwZDZD'
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
        return HttpResponse()

def liste(request):
    minis_list = MiniUrl.objects.order_by('-nb_acces')
    page = request.GET.get('page', 1)
    
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

