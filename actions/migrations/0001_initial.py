# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('verb', models.CharField(max_length=255)),
                ('target_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('target_ct', models.ForeignKey(related_name='target_obj', blank=True, null=True, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='actions')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
