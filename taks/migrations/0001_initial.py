# Generated by Django 3.1.4 on 2020-12-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='downloader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('topic', models.TextField(blank=True, default=None, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]