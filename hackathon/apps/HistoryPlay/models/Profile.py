# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    name = models.CharField(
        verbose_name=_(u'nombre'),
        max_length=150,
    )

    def __unicode__(self):
        return self.name

    class Meta:
        app_label='HistoryPlay'