from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html')

# def logout_view(request):
#     pass

def signup_view(request):
    return render(request, 'accounts/signup.html')