# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('position', models.IntegerField()),
                ('is_checked', models.BooleanField(default=False)),
                ('card', models.ForeignKey(to='bingo.Card')),
            ],
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='field',
            name='field_value',
            field=models.ForeignKey(related_name='field_value', to='bingo.FieldValue'),
        ),
        migrations.AddField(
            model_name='card',
            name='game',
            field=models.ForeignKey(to='bingo.Game'),
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
