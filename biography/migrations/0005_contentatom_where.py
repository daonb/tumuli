# Generated by Django 2.0.1 on 2018-02-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0004_auto_20180206_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentatom',
            name='where',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
