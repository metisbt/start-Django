from django.shortcuts import render
from django.http import HttpResponse
from website.forms import NameForm, ContactFrorm

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            pass


    return render(request, 'website/contact.html')