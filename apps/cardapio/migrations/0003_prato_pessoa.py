# Generated by Django 3.2.6 on 2021-08-17 17:38

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('cardapio', '0002_rename_categria_prato_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),

        ),
    ]