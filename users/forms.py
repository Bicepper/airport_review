from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
)

from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateForm(UserCreationForm):
    """
    ユーザー登録フォーム
    """
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == 'admin' or username == 'Admin' or username == '管理者' or username == '管理人':
            raise forms.ValidationError('このユーザー名は使用できません。')
        return username


class MyPasswordChangeForm(PasswordChangeForm):
    """
    パスワード変更フォーム
    """


class MyPasswordResetForm(PasswordResetForm):
    """
    パスワードを忘れた時のフォーム
    """


class MySetPasswordForm(SetPasswordForm):
    """
    パスワード再設定フォーム
    """