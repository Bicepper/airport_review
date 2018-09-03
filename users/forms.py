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