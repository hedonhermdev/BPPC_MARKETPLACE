# Generated by Django 2.1.5 on 2020-03-29 06:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200329_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
