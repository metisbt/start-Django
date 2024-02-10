from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        msg = 'user is not authenticated!'
    
    context = {'msg' : msg}
    return render(request, 'accounts/login.html', context)

# def logout_view(request):
#     pass

def signup_view(request):
    return render(request, 'accounts/signup.html')