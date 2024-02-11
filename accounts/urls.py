from django.urls import path
from accounts.views import *
# from django.contrib.auth.views import (
#     PasswordResetView, 
#     PasswordResetDoneView, 
#     PasswordResetConfirmView,
#     PasswordResetCompleteView
# )



app_name = 'accounts'

urlpatterns = [
    # login
    path('login/', login_view, name='login'),
    # logout
    path('logout/', logout_view, name='logout'),
    # register / signup
    path('signup/', signup_view, name='signup'),
    # forgot password
    # path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    # path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]