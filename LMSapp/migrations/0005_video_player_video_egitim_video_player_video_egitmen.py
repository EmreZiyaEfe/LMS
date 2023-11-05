# Generated by Django 4.2.5 on 2023-11-04 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LMSapp', '0004_alter_video_player_video_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_player',
            name='video_egitim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LMSapp.egitimler'),
        ),
        migrations.AddField(
            model_name='video_player',
            name='video_egitmen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]