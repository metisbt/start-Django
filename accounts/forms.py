from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username','password']

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].label = 'Email or Username'

class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  