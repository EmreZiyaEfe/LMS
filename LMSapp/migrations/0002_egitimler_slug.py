# Generated by Django 4.2.5 on 2023-11-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='egitimler',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]