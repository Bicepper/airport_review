# Generated by Django 2.1.1 on 2018-10-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('username', models.CharField(max_length=32, null=True, unique=True, verbose_name='ユーザー名')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('is_active', models.BooleanField(default=True, verbose_name='有効・無効')),
                ('is_staff', models.BooleanField(default=False, verbose_name='スタッフ')),
                ('url', models.URLField(blank=True)),
                ('intro', models.TextField(blank=True, verbose_name='自己紹介')),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'ユーザー',
                'verbose_name_plural': 'ユーザー',
            },
        ),
    ]
