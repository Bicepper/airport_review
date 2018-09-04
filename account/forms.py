from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    """
    ユーザー情報更新
    """
    class Meta:
        model = User
        fields = ('username', 'email')