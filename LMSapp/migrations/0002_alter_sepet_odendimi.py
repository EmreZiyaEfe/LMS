# Generated by Django 4.2.5 on 2023-11-06 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sepet',
            name='odendiMi',
            field=models.BooleanField(default=False, verbose_name='Ödendi mi?'),
        ),
    ]
