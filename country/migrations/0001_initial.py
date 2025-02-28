# Generated by Django 2.0.2 on 2018-11-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ja', models.CharField(max_length=255, verbose_name='国名：日本語')),
                ('name_en', models.CharField(max_length=255, verbose_name='国名：英語')),
                ('code_two', models.CharField(max_length=2, verbose_name='国名コード：2桁')),
                ('code_three', models.CharField(max_length=3, verbose_name='国名コード：3桁')),
            ],
            options={
                'verbose_name': '国',
                'verbose_name_plural': '国',
            },
        ),
    ]
