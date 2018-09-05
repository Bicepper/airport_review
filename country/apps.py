from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CountryConfig(AppConfig):
    name = 'country'
    verbose_name = _('国')
