# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171001_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=datetime.datetime(2017, 10, 1, 23, 48, 7, 284416, tzinfo=utc), upload_to='images'),
            preserve_default=False,
        ),
    ]
