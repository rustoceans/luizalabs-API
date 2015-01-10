from django.test import TestCase
from django.test import Client
from luizalabs.consuming_facebook.forms import PersonForm

# Create your tests here.

"""

Testing Home url and form.field of page.

"""


class TestHome(TestCase):

    def setUp(self):
        self.c = Client()
        self.resp = self.c.get('/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'home.html')

    def test_form_has_fields(self):
        form = PersonForm()
        self.assertItemsEqual(['facebook_id'], form.fields)

    def test_facebook_id_is_digit(self):
        form = self.make_validated_form(facebook_id='ITSsNOT')
        self.assertItemsEqual(['facebook_id'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(facebook_id='654')
        data.update(kwargs)
        form = PersonForm(data)
        form.is_valid()
        return form
