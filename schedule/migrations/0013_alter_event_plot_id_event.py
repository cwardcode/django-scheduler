# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_event_calendar_not_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='plot_id',
            field=models.CharField(verbose_name='Plot ID', max_length=20, blank=True),
        ),
    ]
