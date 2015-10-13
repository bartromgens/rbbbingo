# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


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
            field=django_resized.forms.ResizedImageField(upload_to='', blank=True),
        ),
    ]
