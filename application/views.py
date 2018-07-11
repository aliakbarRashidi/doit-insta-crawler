from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import redirect
from instagram.client import InstagramAPI
import requests
import httplib2
import json
import sys

from .models import Account as Accounts
from .models import ConnectionObject
from .forms import Accounts as Accounts_form
from .forms import addAccount as addAccount
from .forms import addAccount as updateAccount
from .forms import Tag as Tag_form
from .instaapi import InstaApi
from .ParseHTML import ParseHTML

from collections import Counter

def check_connections():
    my_connections = {}
    all_entries = Accounts.objects.all()

    i=0
    while i<all_entries.count():
        #try to connect to your accounts
        account = all_entries[i]

        if account.host == 'instagram':
            instagram_api_url = 'https://api.instagram.com/oauth/authorize/?client_id='+account.key_1+'&redirect_uri='+account.key_3+'&response_type=code'
            try:
                instagram_response = requests.get(instagram_api_url)
                
                if instagram_response.status_code == 200:
                    my_connections[account.name]='connected'
                if instagram_response.status_code > 200:
                    my_connections[account.name]='failed'
            except Exception as e:
                my_connections[account.name]='error'
                print(str(e))
            
        elif account.host == 'facebook':
            pass
            """
            facebook_api_url = 'https://api.instagram.com/oauth/authorize/?client_id='+account.key_1+'&redirect_uri='+account.key_3+'&response_type=code'
            try:
                facebook_response = requests.get(facebook_api_url)
                if facebook_response.status_code == 200:
                    my_connections.append([account.name, 'facebook', 'connected'])
                else: my_connections.append([account.name, 'facebook', 'connection failed'])
            except Exception as e:
                my_connections.append([account.name, 'facebook', 'connection error'])
                print(str(e))    
            """
        i+=1
    
    return my_connections

def dashboard(request):

    my_connections=check_connections()
    #facebook = check_connections()[0]
    
    assert isinstance(request, HttpRequest)
    return render(
            request,
            'dashboard.html',
            {
                'title':'updated',
                'connection_status': my_connections,
               # 'facebook_status':facebook,
            }
        )

def accounts(request):
    my_connections=check_connections()
    if request.method == 'POST':
        form = Accounts_form(request.POST)
        print(form.data['accounts_form'])
        if form.is_valid():
            #Renders the whois page.
            print('form is valid')
            
            filter_name = Accounts.objects.all().filter(name__contains=form.data['accounts_form'])
            filter_username = Accounts.objects.all().filter(username__contains=form.data['accounts_form'])
            filter_host = Accounts.objects.all().filter(host__contains=form.data['accounts_form'])
            filter_port = Accounts.objects.all().filter(port__contains=form.data['accounts_form'])
            filter_key_1 = Accounts.objects.all().filter(key_1__contains=form.data['accounts_form'])
            filter_key_2 = Accounts.objects.all().filter(key_2__contains=form.data['accounts_form'])
            filter_key_3 = Accounts.objects.all().filter(key_3__contains=form.data['accounts_form'])

            #all_results = list(chain(filter_name, filter_username, filter_host, filter_port, filter_key_1, filter_key_2))

            
            result_list = filter_name.union(filter_name, filter_username)
            result_list = result_list.union(result_list, filter_host)
            result_list = result_list.union(result_list, filter_port)
            result_list = result_list.union(result_list, filter_key_1)
            result_list = result_list.union(result_list, filter_key_2)
            result_list = result_list.union(result_list, filter_key_3)
            
            print(result_list)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'accounts.html',
                {
                    'title':'Services',
                    'message': result_list,
                    'connection_status': my_connections,

                }
            )
            
            
        else:
            print('Not valid form.')
            all_entries = Accounts.objects.all()
            return render(
                request,
                'accounts.html',
                {
                    'title':'Services',
                    'message': all_entries,
                    'connection_status': my_connections,

                }
            )
    else:
        all_entries = ""
        string = ""
        all_entries = Accounts.objects.all()
        return render(
            request,
            'accounts.html',
            {
                'title':'Services',
                'message': all_entries,
                'connection_status': my_connections,

            }
        )

def add_account(request):
 
    if request.method == 'POST':
        if request.POST.get('save_save',''):
            form = addAccount(request.POST)
            srv = Accounts.objects.create(name = form.data['name'],
                                              username=form.data['username'],
                                              password=form.data['password'],
                                              host=form.data['host'],
                                              port=form.data['port'],
                                              key_1=form.data['key_1'],
                                              key_2=form.data['key_2'],
                                              key_3=form.data['key_3'])
        
            assert isinstance(request, HttpRequest)
            return redirect('accounts')
        
        if request.POST.get('cancel_save',''):
            assert isinstance(request, HttpRequest)
            return redirect('accounts')

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'add_account.html',
        {
            'title':'Add service',

            
            
        }
    )

def delete_account(request, id):
    acc = Accounts.objects.get(pk = id)
    acc.delete()

            
    assert isinstance(request, HttpRequest)
    return redirect('accounts')

def update_account(request, id):
   
    acc = Accounts.objects.get(pk = id)
    if request.method == 'POST':
        if request.POST.get('edit_save',''):  
            acc = Accounts.objects.get(pk = id)
            form = updateAccount(request.POST)
            acc.name = form.data['name']
            acc.username=form.data['username']
            acc.password=form.data['password']
            acc.host=form.data['host']
            acc.port=form.data['port']
            acc.key_1=form.data['key_1']
            acc.key_2=form.data['key_2']
            acc.key_3=form.data['key_3']
            acc.save()
            
            acc = Accounts.objects.get(pk = id)
            print(acc)
            assert isinstance(request, HttpRequest)
            return render(
                request,
                'update_account.html',
                {
                    'title':'updated',
                    'message': acc,
                    'message_success': 'Updated!',
             
                }
            )
        elif request.POST.get('delete_save',''):
            acc = Accounts.objects.get(pk = id)
            acc.delete()
            all_entries = Accounts.objects.all()
            assert isinstance(request, HttpRequest)
            return redirect('accounts')
        
        elif request.POST.get('cancel_save',''):
            assert isinstance(request, HttpRequest)
            return redirect('accounts')
                    

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'update_account.html',
        {
            'title':'Edit',
            'message': acc,
  
        }
    )

def find_and_like_by_tag(request):
    #get accounts from db
    all_accounts = Accounts.objects.all()

    obj='empty'
    try:
        obj = TheBot.login_to_instagram('krregg','gerimon12')
    except Exception as e:
        print(str(e))




    #disply by default
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'find-and-like-by-tag.html',
        {
            'title': 'updated',
            'message': obj,
            'account_list': all_accounts,
        }
    )

def work_with_account(request, id):

    #get latest entry from db



    acc = Accounts.objects.get(pk=id)

    obj_connection = ConnectionObject()
    acc = Accounts.objects.get(pk=id)
    obj = InstaApi()
    obj.login_to_instagram(acc.username, acc.password)
    if request.method == 'POST':
        if request.POST.get('like_by_tag', ''):
            form = Tag_form(request.POST)
            like_posts_by_tag(form.data['tag_name'],form.data['tag_number'])
            return render(
                request,
                'work-with-account.html',
                {
                    'title': 'search',
                    'account': acc,
                    'message': obj.status,
                   # 'followers': followers,

                }
            )

        if request.POST.get('cancel_back',''):
            return redirect('find_and_like_by_tag')


    return render(
        request,
        'work-with-account.html',
        {
            'title': 'display',
            'account': acc,
            'message': obj.status,
            #'followers': followers,
        }
    )

def like_posts_by_tag(tags,post_number):
    tag_url = 'https://www.instagram.com/explore/tags/'

    response = requests.post(tag_url+tags)
    print(response.content.decode('utf-8'))
