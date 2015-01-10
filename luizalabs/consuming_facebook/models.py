# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):

    name = models.CharField(_(u'Name'), max_length=100, default="",
                            blank=True, null=True)

    facebook_id = models.CharField(_(u'Facebook ID'), max_length=30,
                                   blank=True,
                                   null=True)

    gender = models.CharField(_(u'Gender'), max_length=10,
                              blank=True, null=True)

    class Meta:
        verbose_name = _(u'Person')
        verbose_name_plural = _(u'Persons')
        ordering = ['facebook_id']

    def __unicode__(self):
        return u'{username} (Facebook ID: {facebook_id})'.format(
            username=self.username,
            facebook_id=self.facebook_id
        )

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username
