"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html')),
    path('customers/',TemplateView.as_view(template_name = 'customers.html')),
    path('products/',TemplateView.as_view(template_name = 'products.html')),
    path('login/',TemplateView.as_view(template_name = 'login.html')),
    path('register/',TemplateView.as_view(template_name = 'register.html')),
    path('account/',TemplateView.as_view(template_name = 'account.html')),
    path('settings/',TemplateView.as_view(template_name = 'settings.html')),
    path('404/',TemplateView.as_view(template_name = '404.html')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_URL)
