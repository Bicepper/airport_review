# Generated by Django 2.1.1 on 2018-10-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_review_img_01'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_img_01',
            field=models.FileField(blank=True, upload_to='static/img/review', verbose_name='画像1'),
        ),
    ]
