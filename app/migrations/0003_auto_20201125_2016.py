# Generated by Django 3.1.3 on 2020-11-26 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20201125_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos_usuario',
            name='username',
        ),
        migrations.AddField(
            model_name='datos_usuario',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
