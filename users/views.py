from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.core.signing import BadSignature
from django.core.signing import SignatureExpired
from django.core.signing import loads
from django.core.signing import dumps
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)

from .forms import (
    UserCreateForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
)

User = get_user_model()  # プロジェクトで使用しているUserモデルを取得


class UserCreate(generic.CreateView):
    """
    ユーザー仮登録
    """
    template_name = 'register/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        """
        仮登録と本登録メールの発行
        """
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # アクティベーションURL送付
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject_template = get_template('temporary_registration/mail/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('temporary_registration/mail/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)
        return redirect('create_done')


class UserCreateDone(generic.TemplateView):
    """
    ユーザー仮登録完了
    """
    template_name = 'temporary_registration/user_create_done.html'


class UserCreateComplete(generic.TemplateView):
    """
    ユーザー本登録
    """
    template_name = 'temporary_registration/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # 24時間で期限切れ

    def get(self, request, **kwargs):
        """
        tokenが正しければ本登録
        """
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが違う
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


# class PasswordChange(PasswordChangeView):
#     """
#     パスワード変更
#     """
#     form_class = MyPasswordChangeForm
#     success_url = reverse_lazy('password_reset_done')
#     template_name = 'reset/password_reset.html'
#
#
# class PasswordChangeDone(PasswordChangeDoneView):
#     """
#     パスワード変更完了
#     """
#     template_name = 'reset/password_reset_complete.html'


class PasswordReset(PasswordResetView):
    """
    パスワード変更用URL送付
    """
    subject_template_name = 'reset/password_reset_subject.txt'
    email_template_name = 'reset/password_reset_message.txt'
    template_name = 'reset/password_reset.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """
    パスワード変更用URL送付済み
    """
    template_name = 'reset/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """
    新パスワード入力
    """
    form_class = MySetPasswordForm
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'reset/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """
    新パスワード設定完了
    """
    template_name = 'reset/password_reset_complete.html'
