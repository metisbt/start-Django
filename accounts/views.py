from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import SignupForm, CustomLoginForm




def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        
        form = CustomLoginForm()
        context = {'form' : form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

        form = SignupForm()

        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
    

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

        form = SignupForm()

        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')