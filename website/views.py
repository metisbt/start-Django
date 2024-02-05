from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import NameForm, ContactFrorm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactFrorm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your message has sent successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Your message send failed!")

    form = ContactFrorm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
