# Generated by Django 2.0.1 on 2018-03-01 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biography', '0005_contentatom_where'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentatom',
            name='image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='photologue.Photo'),
        ),
    ]
