"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap
from django.urls import include, path
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import re_path
from django.views.generic.base import TemplateView


sitemaps = {
    "static": StaticViewSitemap,
    'blog' : BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # path('maintenance/', include('maintenance.urls')),
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", include('robots.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path("summernote/", include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    # forgot password
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

]

#for statics
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.MAINTENANCE_MODE:
   urlpatterns.insert(0, re_path(r'^', TemplateView.as_view(template_name='config/maintenance.html'), name='maintenance'))