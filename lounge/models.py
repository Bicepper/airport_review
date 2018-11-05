from django.db import models
from django.utils.translation import ugettext_lazy as _

from airport.models import Airport
from airline.models import Airline
from alliance.models import Alliance


class Lounge(models.Model):
    FLAG = (
        ('0', '無効'),
        ('1', '有効')
    )

    name_flag = models.CharField(_('自由名称フラグ：ラウンジ名の日本語・英語を利用する場合は有効化'), blank=False, max_length=2,
                                 choices=FLAG, default='0')
    name_ja = models.CharField(_('ラウンジ名：日本語'), max_length=255, blank=True, default='')
    name_en = models.CharField(_('ラウンジ名：英語'), max_length=255, blank=True, default='')
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name=_('空港'), null=False, default='')
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, verbose_name=_('航空会社'), null=True, blank=True)
    # alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE, verbose_name=_('アライアンス'), null=True, blank=True)

    main_image = models.ImageField(_('メイン画像'), upload_to='static/img/lounge/main', blank=True)

    class Meta:
        verbose_name = _('ラウンジ')
        verbose_name_plural = _('ラウンジ')

    def __str__(self):
        return '{a} {b}'.format(a=self.airport, b=self.airline)
