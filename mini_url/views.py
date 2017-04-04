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

