from django.db import models
from django.utils.translation import ugettext_lazy as _


class Alliance(models.Model):
    name_ja = models.CharField(_('アライアンス名：日本語'), max_length=255, blank=False)
    name_en = models.CharField(_('アライアンス名：英語'), max_length=255, blank=False)
    establish_date = models.DateTimeField(_('設立日'), blank=False)
    main_image = models.ImageField(_('ロゴ画像'), upload_to='static/img/alliance')
    url = models.URLField(_('WebサイトURL'), blank=False, default='')

    class Meta:
        verbose_name = _('アライアンス')
        verbose_name_plural = _('アライアンス')

    def __str__(self):
        return self.name_ja
