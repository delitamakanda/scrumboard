from django.shortcuts import render, get_object_or_404, redirect
from .models import MiniUrl
from .forms import MiniUrlForm, ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, mail_admins#, send_email
from django.template import Context
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.loader import get_template #send a .txt template
from django.contrib import messages

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


def contact_us_view(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content
            })

            content = template.render(context)

            email = EmailMessage(
                "Nouveau message de Shorten app",
                content,
                "Shorten app" + '',
                ['delita.makanda@gmail.com'],
                headers = { 'Reply-To': contact_email }
            )

            email.send()
            return redirect('/contact')

    return render(request, 'mini_url/contact.html', {'form': form_class})
