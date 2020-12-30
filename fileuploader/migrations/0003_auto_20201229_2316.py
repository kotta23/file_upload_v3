# Generated by Django 3.1.4 on 2020-12-29 23:16

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileuploader', '0002_designfile_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='designfile',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='designfile',
            name='file',
            field=models.FileField(upload_to='designs', validators=[django.core.validators.FileExtensionValidator(['xml'])]),
        ),
    ]
