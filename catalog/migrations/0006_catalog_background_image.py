# Generated by Django 3.0.1 on 2021-06-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20210621_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='background_image',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
