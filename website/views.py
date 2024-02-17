from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages



def maintenance(request):
    return render(request, 'config/maintenance.html')

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.name = 'unkonown'
            new.save()
            messages.add_message(request, messages.SUCCESS, "Your message has sent successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Your message send failed!")

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
