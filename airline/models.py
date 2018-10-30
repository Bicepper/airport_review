from django.db import models
from django.utils.translation import ugettext_lazy as _

from alliance.models import Alliance
from country.models import Country


class Airline(models.Model):
    name_ja = models.CharField(_('航空会社：日本語'), max_length=255, blank=False)
    name_en = models.CharField(_('航空会社：英語'), max_length=255, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_('国'), null=False, default='')
    iata = models.CharField(_('IATA'), max_length=2, blank=False)
    icao = models.CharField(_('ICAO'), max_length=3, blank=False)
    url = models.URLField(_('WebサイトURL'), blank=False, default='')
    member_alliance = models.ForeignKey(Alliance, on_delete=models.CASCADE, verbose_name=_('加盟アライアンス'),
                                        null=False, default='')
    main_image = models.ImageField(_('ロゴ画像'), upload_to='static/img/airline', blank=False)

    class Meta:
        verbose_name = _('航空会社')
        verbose_name_plural = _('航空会社')

    def __str__(self):
        return self.name_ja

