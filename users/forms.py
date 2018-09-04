from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
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

