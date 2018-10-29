# Generated by Django 2.0.2 on 2018-10-27 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alliance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ja', models.CharField(max_length=255, verbose_name='航空会社：日本語')),
                ('name_en', models.CharField(max_length=255, verbose_name='航空会社：英語')),
                ('establish_date', models.DateField(verbose_name='設立日')),
                ('main_image', models.ImageField(upload_to='static/img/airline', verbose_name='ロゴ画像')),
                ('iata', models.CharField(max_length=2, verbose_name='IATA')),
                ('icao', models.CharField(max_length=3, verbose_name='ICAO')),
                ('url', models.URLField(default='', verbose_name='WebサイトURL')),
                ('member_alliance', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='alliance.Alliance', verbose_name='加盟アライアンス')),
            ],
            options={
                'verbose_name': '航空会社',
                'verbose_name_plural': '航空会社',
            },
        ),
    ]
