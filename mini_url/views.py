from django.shortcuts import render, get_object_or_404, redirect
from .models import MiniUrl
from .forms import MiniUrlForm
from django.views.generic.base import TemplateView

def liste(request):
    minis = MiniUrl.objects.order_by('-nb_acces')
    return render(request, 'mini_url/liste.html', locals())

def nouveau(request):
    if request.method == 'POST':
        form = MiniUrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = MiniUrlForm()
    return render(request, 'mini_url/nouveau.html', {'form' : form})

def redirection(request, code):
    mini = get_object_or_404(MiniUrl, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)


class ContactView(TemplateView):
    pass
