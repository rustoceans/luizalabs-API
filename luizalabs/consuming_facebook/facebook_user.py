# coding: utf-8
import urllib2
import json
import collections


class Consuming:

    def __init__(self, FACEBOOK_ID):
        self.FACEBOOK_ID = FACEBOOK_ID
        self.url = 'https://graph.facebook.com/{FACEBOOK_ID}'.format(
            FACEBOOK_ID=FACEBOOK_ID)
        self.response = urllib2.urlopen(self.url)

    def user(self):
        response_read = self.response.read()
        user_response = json.loads(response_read)
        return user_response

    def convert(self, data):
        if isinstance(data, basestring):
            return str(data)
        elif isinstance(data, collections.Mapping):
            return dict(map(self.convert, data.iteritems()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(self.convert, data))
        else:
            return data

    def decode_users(self):
        convert = self.convert(self.user())
        return convert
