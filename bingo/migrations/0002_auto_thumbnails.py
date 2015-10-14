# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bingo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldvalue',
            options={'verbose_name': 'Event'},
        ),
        migrations.AlterField(
            model_name='fieldvalue',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to=''),
        ),
    ]
