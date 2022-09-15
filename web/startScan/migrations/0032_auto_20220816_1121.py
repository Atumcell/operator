# Generated by Django 3.2.4 on 2022-08-16 11:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0031_auto_20220803_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanhistory',
            name='dir_file_fuzz',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='fetch_url',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='http_crawl',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='osint',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='port_scan',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='screenshot',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='subdomain_discovery',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='vulnerability_scan',
        ),
        migrations.RemoveField(
            model_name='scanhistory',
            name='waf_detection',
        ),
        migrations.AddField(
            model_name='scanhistory',
            name='tasks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='scanhistory',
            name='scan_status',
            field=models.IntegerField(choices=[(-1, -1), (0, 0), (1, 1), (2, 2), (3, 3)], default=-1),
        ),
    ]