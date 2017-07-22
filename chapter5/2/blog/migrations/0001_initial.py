# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text=b'blogs title', max_length=30, unique=True, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('body', models.TextField(verbose_name='content')),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blog_plural',
            },
        ),
    ]