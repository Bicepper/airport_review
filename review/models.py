from django.db import models
from django.utils.translation import ugettext_lazy as _

from airport.models import Airport


class Review(models.Model):
    RATE_NUM = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('1', '10'),
    )
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, verbose_name=_('空港'))
    rate_clean = models.CharField(_('清潔さ'), max_length=2, blank=False, choices=RATE_NUM, default=None)
