# Generated by Django 4.0.6 on 2022-07-27 23:10

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0008_pop_user_who_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='pop',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pop',
            name='pop_image',
            field=models.ImageField(blank=True, null=True, upload_to='popimg'),
        ),
        migrations.AddField(
            model_name='pop',
            name='save_user',
            field=models.ManyToManyField(blank=True, related_name='save_pop', to=settings.AUTH_USER_MODEL),
        ),
    ]
