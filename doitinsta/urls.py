"""doitinsta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path
import application.views
import application.forms
import django.contrib.auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', application.views.dashboard, name='dashboard'),

    path('accounts/', application.views.accounts, name='accounts'),
    path('accounts/add_account/', application.views.add_account, name='add_account'),
    path('find-and-like-by-tag/', application.views.find_and_like_by_tag, name='find_and_like_by_tag'),

    re_path(r'^accounts/update_account/(?:acc-(?P<id>\d+)/)?$', application.views.update_account, name='update_account'),
    re_path(r'^accounts/delete_account/(?:acc-(?P<id>\d+)/)?$', application.views.delete_account, name='delete_account'),
    re_path(r'^find-and-like-by-tag/work-with-account/(?:acc-(?P<id>\d+)/)', application.views.work_with_account, name='work-with-account'),



    path('login/',
        django.contrib.auth.views.login,
        {
            'template_name': 'login.html',
            'authentication_form': application.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                
            }
        },
        name='login'),
    path('logout',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
]

