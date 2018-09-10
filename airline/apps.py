from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AirlineConfig(AppConfig):
    name = 'airline'
    verbose_name = _('航空会社')

