# Generated by Django 3.0.1 on 2021-06-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210621_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='bio',
            field=models.TextField(max_length=2500),
        ),
    ]