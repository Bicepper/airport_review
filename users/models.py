from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser  # ユーザー完全カスタマイズ
from django.contrib.auth.models import PermissionsMixin  # Djangoの権限フレームワークを独自のユーザークラスに組み込む
from django.utils.translation import ugettext_lazy as _
import pytz

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('メールアドレス'), unique=True, blank=False)
    username = models.CharField(_('ユーザー名'), max_length=32, unique=True, blank=False, null=True)
    date_joined = models.DateTimeField(_('登録日'), auto_now_add=True)
    is_active = models.BooleanField(_('有効・無効'), default=True)
    is_staff = models.BooleanField(_('スタッフ'), default=False)
    url = models.URLField(blank=True)
    intro = models.TextField(_('自己紹介'), blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    class Meta:
        verbose_name = _('ユーザー')
        verbose_name_plural = _('ユーザー')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        ユーザーにメール送信
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
