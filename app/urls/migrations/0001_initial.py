# Generated by Django 4.2 on 2023-05-13 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=20, verbose_name='PID')),
                ('long_url', models.TextField(verbose_name='Long Url')),
                ('short_url', models.CharField(max_length=200, verbose_name='Short Url')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
            ],
        ),
        migrations.CreateModel(
            name='SingleLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_id', models.CharField(max_length=20, verbose_name='SID')),
                ('single_link', models.CharField(max_length=200, verbose_name='Single Link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('short_url', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='urls.url')),
            ],
        ),
    ]
