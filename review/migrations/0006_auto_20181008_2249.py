# Generated by Django 2.0.2 on 2018-10-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20181008_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_title',
            field=models.CharField(default='', max_length=40, verbose_name='タイトル'),
        ),
    ]
