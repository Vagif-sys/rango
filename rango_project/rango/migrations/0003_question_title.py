# Generated by Django 3.0.1 on 2020-10-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20201026_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='default title', max_length=200),
            preserve_default=False,
        ),
    ]
