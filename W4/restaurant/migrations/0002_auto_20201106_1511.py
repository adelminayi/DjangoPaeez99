# Generated by Django 3.1.2 on 2020-11-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='rate',
            field=models.FloatField(default=5),
        ),
    ]
