from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        verbose_name=_(u'Categoria'),
        max_length=150,
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

