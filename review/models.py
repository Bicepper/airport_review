from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

from users.models import User
from airport.models import Airport


class Review(models.Model):
    RATE_NUM = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    user = models.ManyToManyField(User, default=None)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name=_('空港'))
    rate_clean = models.CharField(_('清潔さ'), max_length=2, blank=False, choices=RATE_NUM, default=None)
    rate_facility = models.CharField(_('施設・設備'), max_length=2, blank=False, choices=RATE_NUM, default=None)
    rate_lounge = models.CharField(_('ラウンジ'), max_length=2, blank=False, choices=RATE_NUM, default=None)
    rate_service = models.CharField(_('サービス'), max_length=2, blank=False, choices=RATE_NUM, default=None)
    rate_access = models.CharField(_('アクセス'), max_length=2, blank=False, choices=RATE_NUM, default=None)
    review_date = models.DateTimeField(_('登録日'), auto_now_add=True)
    review_update = models.DateTimeField(_('更新日'), auto_now=True)
    review_title = models.CharField(_('タイトル'), max_length=40, blank=False, default="")
    review_text = models.TextField(_('レビュー'), max_length=1000, blank=False, default="")





