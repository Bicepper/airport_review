# Generated by Django 2.1.1 on 2018-10-09 06:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
