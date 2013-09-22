from django.db import models
from django.utils.translation import ugettext_lazy as _


class HistoryPlay(models.Model):
    STATUS_COMPLETE = 1
    STATUS_INCOMPLETE = 0

    STATUS_CHOICES = (
        (STATUS_COMPLETE, _('Completado')),
        (STATUS_INCOMPLETE, _('Incompleto')),
    )

    name = models.CharField(
        verbose_name=_(u'Pregunta'),
        max_length=150,
    )
    place = models.ForeignKey (
        'Place',
        verbose_name=_(u'lugar'),
        related_name='history_play_set'
    )
    profile = models.ForeignKey (
        'Profile',
        verbose_name=_(u'perfil'),
        related_name='history_play_set'
    )
    progress = models.IntegerField(
        verbose_name=_(u'progreso'),
        max_value = 100,
        min_value = 0
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_INCOMPLETE,
        editable=False,
        null=False,
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
        return self.street[:30]

    class Meta:
        app_label='hp'