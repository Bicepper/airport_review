from django.contrib.auth.base_user import BaseUserManager  # ユーザーモデルがカスタマイズされる場合、マネージャも必要


class UserManager(BaseUserManager):
    use_in_migration = True  # manage.pyで利用可能にする

    def _create_user(self, email, password, **extra_fields):
        """
        指定された電子メールとパスワードでユーザーを作成し、保存
        """
        if not email:  # メールアドレスが指定されていなかった場合
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)  # メールアドレスを正規化
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  # 指定するDBに保存
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        is_staff（管理サイトへのログイン可否）と、is_superuser（全権付与）をFalseに設定
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        スーパーユーザーは、is_staffとis_superuserをTrueに設定
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
