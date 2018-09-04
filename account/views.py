from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import resolve_url
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin  # ログイン済み、かつ条件を満たしているか
from django.views import generic


User = get_user_model()


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        """
        現在ログインしているユーザーのPKと、表示しているマイページのPKが同一か判定
        スーパーユーザーは無条件で表示
        """
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class Account(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'account/user_detail.html'

