from django import forms
from luizalabs.consuming_facebook.models import Person
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def FacebookIDValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'Sorry, just numbers!'))


class PersonForm(forms.ModelForm):
    facebook_id = forms.IntegerField(widget=forms.NumberInput(attrs={
        'required': 'required=True', 'name': 'facebook_id'}))

    class Meta:
        model = Person
        fields = ['facebook_id']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['facebook_id'].validators.append(FacebookIDValidator)
