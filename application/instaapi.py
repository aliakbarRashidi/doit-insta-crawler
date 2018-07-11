
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


from InstagramAPI import InstagramAPI

class InstaApi:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.status = 'Not connected'

        self.api = None #main object

    def login_to_instagram(self,username, password):

        self.username = username
        self.password = password

        self.api = InstagramAPI(self.username, self.password)
        if (self.api.login()):

            self.api.getSelfUserFeed()  # get self user feed
            #print(self.api.LastJson)  # print last response JSON
            self.status="Login succes!"

        else:
            self.status ="Can't login!"

    def get_total_followers(self):
        """
        Returns the list of followers of the user.
        It should be equivalent of calling api.getTotalFollowers from InstagramAPI
        """

        followers = []
        next_max_id = True
        user_id = self.api.username_id

        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = self.api.getUserFollowers(user_id, maxid=next_max_id)
            followers.extend(self.api.LastJson.get('users', []))
            next_max_id = self.api.LastJson.get('next_max_id', '')
        return followers
