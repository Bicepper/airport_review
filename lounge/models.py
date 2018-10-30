from django.db import models
from django.utils.translation import ugettext_lazy as _

from airport.models import Airport
from airline.models import Airline


class Lounge(models.Model):
    name_ja = models.CharField(_('ラウンジ名：日本語'), max_length=255, blank=False, default='')
    name_en = models.CharField(_('ラウンジ名：英語'), max_length=255, blank=False, default='')
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name=_('空港'), null=False, default='')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, verbose_name=_('航空会社'), null=True, blank=True)
    main_image = models.ImageField(_('メイン画像'), upload_to='static/img/lounge/main', blank=True)

    class Meta:
        verbose_name = _('ラウンジ')
        verbose_name_plural = _('ラウンジ')

    def __str__(self):
        return self.name_ja
