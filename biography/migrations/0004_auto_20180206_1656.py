# Generated by Django 2.0.1 on 2018-02-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0003_auto_20180206_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='memoir',
            name='notes',
            field=models.TextField(blank=True, help_text='notes by and for the biographer', verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='period',
            name='notes',
            field=models.TextField(blank=True, help_text='notes by and for the biographer', verbose_name='Notes'),
        ),
    ]
