from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import NameForm, ContactFrorm, NewsletterForm

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactFrorm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('Not valid!')

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
