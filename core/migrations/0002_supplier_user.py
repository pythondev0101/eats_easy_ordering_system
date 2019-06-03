# Generated by Django 2.1.5 on 2019-05-12 08:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='user',
            field=models.ManyToManyField(related_name='supplier_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
