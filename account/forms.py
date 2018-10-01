from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()


class UserUpdateForm(forms.ModelForm):
    """
    ユーザー情報更新
    """
    class Meta:
        model = User
        fields = ('email', )


class UserUpdateEmailForm(forms.ModelForm):
    """
    ユーザー情報更新：メール
    """
    class Meta:
        model = User
        fields = ('email', )


class UserUpdateIntroForm(forms.ModelForm):
    """
    ユーザー情報更新：自己紹介
    """
    class Meta:
        model = User
        fields = ('intro', )


class UserUpdateSocialmediaForm(forms.ModelForm):
    """
    ユーザー情報更新：SNS
    """
    class Meta:
        model = User
        fields = ('facebook', 'twitter', 'youtube', 'instagram', )