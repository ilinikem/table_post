# Generated by Django 3.1.4 on 2020-12-24 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taks', '0003_auto_20201224_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloader',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taks.user'),
        ),
    ]