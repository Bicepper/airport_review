from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    name_ja = models.CharField(_('国名：日本語'), max_length=255, blank=False)
    name_en = models.CharField(_('国名：英語'), max_length=255, blank=False)
    code_two = models.CharField(_('国名コード：2桁'), max_length=2, blank=False)
    code_three = models.CharField(_('国名コード：3桁'), max_length=3, blank=False)

    class Meta:
        verbose_name = _('国')
        verbose_name_plural = _('国')

    def __str__(self):
        return self.name_ja