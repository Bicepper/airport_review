from django.db import models
from django.utils.translation import ugettext_lazy as _

from alliance.models import Alliance


class Airline(models.Model):
    name_ja = models.CharField(_('航空会社：日本語'), max_length=255, blank=False)
    name_en = models.CharField(_('航空会社：英語'), max_length=255, blank=False)
    establish_date = models.DateField(_('設立日'), blank=False)
    main_image = models.ImageField(_('ロゴ画像'), upload_to='static/img/airline', blank=False)
    iata = models.CharField(_('IATA'), max_length=2, blank=False)
    icao = models.CharField(_('ICAO'), max_length=3, blank=False)
    url = models.URLField(_('WebサイトURL'), blank=False, default='')
    member_alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE, verbose_name=_('加盟アライアンス'),
                                        null=False, default='')

    class Meta:
        verbose_name = _('航空会社')
        verbose_name_plural = _('航空会社')

    def __str__(self):
        return self.name_ja

