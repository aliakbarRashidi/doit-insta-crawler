import atexit
import datetime
import itertools
import json
import random
import signal
import sys
import time
import requests
from lxml import html

class TheBot:
    username = ''
    password = ''
    status = ''

    url = 'https://www.instagram.com/'
    url_tag = 'https://www.instagram.com/explore/tags/%s/?__a=1'
    url_likes = 'https://www.instagram.com/web/likes/%s/like/'
    url_unlike = 'https://www.instagram.com/web/likes/%s/unlike/'
    url_comment = 'https://www.instagram.com/web/comments/%s/add/'
    url_follow = 'https://www.instagram.com/web/friendships/%s/follow/'
    url_unfollow = 'https://www.instagram.com/web/friendships/%s/unfollow/'
    url_login = 'https://www.instagram.com/accounts/login/ajax/'
    url_logout = 'https://www.instagram.com/accounts/logout/'
    url_media_detail = 'https://www.instagram.com/p/%s/?__a=1'
    url_user_detail = 'https://www.instagram.com/%s/'
    api_user_detail = 'https://i.instagram.com/api/v1/users/%s/info/'

    accept_language = 'en-US,en;q=0.5'


    def __init__(self):
        self.username = 'krregg'
        self.password = 'gerimon12'
        self.status= 'theBot is alive!'
        self.content = ''

        #create session
        self.session = requests.session()

        self.session.headers.update({
            'Accept': '*/*',
            'Accept-Language': self.accept_language,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'X-Instagram-AJAX': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
        })
        print('---- calling login to instagram ----')


    def login_to_instagram(self,username, password):
        self.username = username
        self.password = password
        payload = {
            'username':self.username,
            'password': self.password,
            'csrfmiddlewaretoken': '<CSRF_TOKEN>',
        }

        self.session = requests.session()
        login_url = "https://www.instagram.com/accounts/login/ajax/"
        result = self.session.get(login_url)



        result = self.session.post(
            login_url,
            data=payload,
            headers=dict(referer=login_url)
        )

        url = self.url
        result = self.session.get(
            url,
            headers=dict(referer=url)
        )


        self.status=result.status_code

        """self.username=username
        self.password=password
        try:
            req = self.session.get(self.url)
            print(self.session)
            #self.session.headers.update({'X-CSRFToken': req.cookies['csrf_token']})
            login_data ={'username':self.username, 'password':self.password}
            login = self.session.post(self.url, data=login_data, allow_redirects=True)
            #self.session.headers.update({'X-CSRFToken': login.cookies['csrf_token']})
            print(login.status_code)

            cookies = login.cookies
            self.content = login.content

            self.status = json.loads(login.text)
        except Exception as e:
            print(str(e))

        if login.status_code == 200:
            self.status = 'Connection works!'
        else:
            self.status = 'Connection Failed!'
        return  self.status
        """
    def __str__(self):
        return self.status