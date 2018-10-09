# Generated by Django 2.0.2 on 2018-10-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ja', models.CharField(max_length=255, verbose_name='アライアンス名：日本語')),
                ('name_en', models.CharField(max_length=255, verbose_name='アライアンス名：英語')),
                ('establish_date', models.DateTimeField(verbose_name='設立日')),
                ('main_image', models.ImageField(upload_to='static/img/alliance', verbose_name='ロゴ画像')),
                ('url', models.URLField(default='', verbose_name='WebサイトURL')),
            ],
            options={
                'verbose_name': 'アライアンス',
                'verbose_name_plural': 'アライアンス',
            },
        ),
    ]
