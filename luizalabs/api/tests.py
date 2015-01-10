from django.test import TestCase
from django.test import Client
from rest_framework.test import APITestCase
import json

# Create your tests here.


class TestAPI(APITestCase):

    def setUp(self):
        """
            Initializing constants variables that
            use in many tests this classe.
        """

        self.url = '/api/person/'
        self.data = {'facebook_id': '320'}
        self.facebook_id = '320'

        self.like_normal = {"id": 1, "username": "mariu.carlo", "name":
                            "Mariu Carlo", "facebook_id": "320",
                            "gender": "female"}

        self.like_get = {u'count': 1, u'previous': None, u'results': [
                        {u'username': u'mariu.carlo', u'gender': u'female',
                         u'facebook_id': u'320', u'id': 1,
                         u'name': u'Mariu Carlo'}],
                         u'next': None}

        self.c = Client()
        self.response_post = self.c.post(self.url, self.data, format='json')
        self.response_get = self.c.get(self.url)

    def test_post(self):
        self.assertEqual(self.response_post.status_code, 201)
        self.assertEqual(self.response_post.data, self.like_normal)

    def test_get(self):
        self.assertEqual(200, self.response_get.status_code)

    def test_get_json(self):
        self.assertEqual(json.loads(self.response_get.content), self.like_get)

    def test_get_unitUser(self):
        response = self.c.get('/api/person/{0}/'.format(self.facebook_id))
        self.assertEqual(json.loads(response.content), self.like_normal)

    def test_delete_user(self):
        response = self.c.delete(
            '/api/person/{0}/'.format(self.facebook_id),
            follow=False, secure=False)
        self.assertEqual(204, response.status_code)
