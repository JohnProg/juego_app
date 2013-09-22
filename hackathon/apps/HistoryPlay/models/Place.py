from django.db import models
from django.utils.translation import ugettext_lazy as _


class Place(models.Model):
    STATUS_ACTIVE = 1
    STATUS_INACTIVE = 0

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _('activo')),
        (STATUS_INACTIVE, _('inactivo')),
    )
    area = models.CharField(
        verbose_name=_(u'Area'),
        max_length=150,
    )
    name = models.CharField(
        verbose_name=_(u'Nombre'),
        max_length=150,
    )
    category = models.ForeignKey (
        'Category',
        verbose_name=_(u'Category'),
        related_name='place_set'
    )
    description = models.CharField(
        verbose_name=_(u'Descripcion'),
        max_length=150,
    )
    address = models.CharField(
        verbose_name=_(u'Pregunta'),
        max_length=150,
    )
    district = models.CharField(
        verbose_name=_(u'Distrito'),
        max_length=150,
    )
    phone = models.CharField(
        verbose_name=_(u'Telefonos'),
        max_length=150,
    )
    web_page = models.CharField(
        verbose_name=_(u'Pagina Web'),
        max_length=150,
    )
    schedule = models.CharField(
        verbose_name=_(u'Horarios'),
        max_length=150,
    )
    cost = models.CharField(
        verbose_name=_(u'costo'),
        max_length=150,
    )
    latitud = models.CharField(
        verbose_name=_(u'Latitud'),
        max_length=150,
    )
    longitud = models.CharField(
        verbose_name=_(u'lenth'),
        max_length=150,
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
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
        return self.name

    class Meta:
        app_label='HistoryPlay'