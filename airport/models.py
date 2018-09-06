from django.db import models
from django.utils.translation import ugettext_lazy as _

from country.models import Country


class Airport(models.Model):
    name_ja = models.CharField(_('空港名：日本語'), max_length=255, blank=False, default='')
    name_en = models.CharField(_('空港名：英語'), max_length=255, blank=False, default='')
    location = models.CharField(_('所在地'), max_length=255, blank=False, default='')
    coordinate_latitude = models.FloatField(_('座標：緯度'), blank=False, default=0)
    coordinate_longitude = models.FloatField(_('座標：軽度'), blank=False, default=0)
    establish_date = models.DateField(_('設立日'), blank=False)
    open_time = models.DateTimeField(_('営業時間：開始'), blank=False, default='')
    close_time = models.DateTimeField(_('営業時間：終了'), blank=False, default='')
    num_terminals = models.IntegerField(_('ターミナル数'), blank=False, default=0)
    area_breadth = models.FloatField(_('敷地面積'), blank=False, default=0)
    url = models.URLField(_('WebサイトURL'), blank=False, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('国'),
                                null=False, default='')
    main_image = models.ImageField(_('メイン画像'), upload_to='static/img/airport/main', blank=False)

    class Meta:
        verbose_name = _('空港')
        verbose_name_plural = _('空港')

    def __str__(self):
        return self.name_ja
