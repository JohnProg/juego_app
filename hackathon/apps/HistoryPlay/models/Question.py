# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    TYPE_ALTERNATIVE = 1
    TYPE_COMPLETE = 2

    TYPE_CHOICES = (
        (TYPE_ALTERNATIVE, _('Alternativas')),
        (TYPE_COMPLETE, _('Completa')),
    )
    place = models.ForeignKey (
        'Place',
        verbose_name=_(u'Lugar'),
        related_name='question_set'
    )
    name = models.CharField(
        verbose_name=_(u'Pregunta'),
        max_length=150,
    )
    image = models.CharField(
        verbose_name=_(u'Imagen'),
        max_length=150,
    )
    type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=TYPE_COMPLETE,
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
