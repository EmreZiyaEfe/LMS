# Generated by Django 4.2.5 on 2023-11-04 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0003_altcategory_anacategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_player',
            name='video_kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='LMSapp.altcategory'),
        ),
    ]
