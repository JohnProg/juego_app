# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Answer(models.Model):
    name = models.CharField (
        verbose_name=_(u'respuesta'),
        max_length=150,
    )
    answer = models.ForeignKey (
        'Answer',
        verbose_name=_(u'Pregunta'),
        related_name='answer_set'
    )
    image = models.CharField (
        verbose_name=_(u'respuesta'),
        max_length=150,
    )
    is_correct = models.BooleanField (
        editable=False,
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    def __unicode__(self):
        return self.name

    class Meta:
        app_label='HistoryPlay'
