# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-13 17:24
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_is_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u8bfe\u7a0b',
                'proxy': True,
                'verbose_name_plural': '\u8f6e\u64ad\u8bfe\u7a0b',
            },
            bases=('courses.course',),
        ),
        migrations.AddField(
            model_name='course',
            name='detail2',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u5e2e\u52a9\u8be6\u60c5'),
        ),
    ]
