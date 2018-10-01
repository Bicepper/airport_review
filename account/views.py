from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import resolve_url
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin  # ログイン済み、かつ条件を満たしているか
from django.views import generic
from . forms import (
    UserUpdateForm,
    UserUpdateEmailForm,
    UserUpdateIntroForm,
    UserUpdateSocialmediaForm,
)


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


# class Account(OnlyYouMixin, generic.DetailView):
#     model = User
#     template_name = 'account/user_detail.html'

# class Account(OnlyYouMixin, generic.UpdateView):
#     model = User
#     form_class = UserUpdateForm
#     template_name = 'account/user_detail.html'
#
#     def get_success_url(self):
#         return resolve_url('account', pk=self.kwargs['pk'])


# class AccountUpdate(OnlyYouMixin, generic.UpdateView):
#     model = User
#     form_class = UserUpdateForm
#     template_name = 'account/user_form.html'
#
#     def get_success_url(self):
#         return resolve_url('account', pk=self.kwargs['pk'])


class AccountUpdateEmail(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateEmailForm
    template_name = 'account/user_detail.html'

    def get_success_url(self):
        return resolve_url('account_update_email', pk=self.kwargs['pk'])


class AccountUpdateIntro(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateIntroForm
    template_name = 'account/user_detail.html'

    def get_success_url(self):
        return resolve_url('account_update_intro', pk=self.kwargs['pk'])


class AccountUpdateSocialmedia(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateSocialmediaForm
    template_name = 'account/user_detail.html'

    def get_success_url(self):
        return resolve_url('account_update_sns', pk=self.kwargs['pk'])

