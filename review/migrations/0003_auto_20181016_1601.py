# Generated by Django 2.1.1 on 2018-10-16 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate_access',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None, max_length=2, verbose_name='アクセス'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate_clean',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None, max_length=2, verbose_name='清潔さ'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate_facility',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None, max_length=2, verbose_name='施設・設備'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate_lounge',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None, max_length=2, verbose_name='ラウンジ'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate_service',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=None, max_length=2, verbose_name='サービス'),
        ),
    ]
