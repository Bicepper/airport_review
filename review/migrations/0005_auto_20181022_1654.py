# Generated by Django 2.1.1 on 2018-10-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20181022_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_img_01',
            field=models.ImageField(blank=True, upload_to='static/img/review', verbose_name='画像1'),
        ),
    ]
