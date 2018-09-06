from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AirportConfig(AppConfig):
    name = 'airport'
    verbose_name = _('空港')

