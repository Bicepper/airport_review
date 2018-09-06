from django.db import models
from django.utils.translation import ugettext_lazy as _

from country.models import Country


class Airport(models.Model):
    name_ja = models.CharField(_('空港名：日本語'), max_length=255, blank=False, default='')
    name_en = models.CharField(_('空港名：英語'), max_length=255, blank=False, default='')
    iata = models.CharField(_('IATA'), max_length=3, blank=False, default='')
    icao = models.CharField(_('ICAO'), max_length=4, blank=False, default='')
    coordinate_latitude = models.FloatField(_('座標：緯度'), blank=False, default=0)
    coordinate_longitude = models.FloatField(_('座標：経度'), blank=False, default=0)
    open_time = models.TimeField(_('営業時間：開始'), blank=False)
    close_time = models.TimeField(_('営業時間：終了'), blank=False)
    num_terminals = models.IntegerField(_('ターミナル数'), blank=False, default=0)
    area_breadth = models.CharField(_('敷地面積'), max_length=255, blank=False, default='')
    url = models.URLField(_('WebサイトURL'), blank=False, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('国'),
                                null=False, default='')
    main_image = models.ImageField(_('メイン画像'), upload_to='static/img/airport/main', blank=True)

    class Meta:
        verbose_name = _('空港')
        verbose_name_plural = _('空港')

    def __str__(self):
        return self.name_ja
