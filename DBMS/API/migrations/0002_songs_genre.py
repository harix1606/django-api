# Generated by Django 3.0 on 2019-12-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='genre',
            field=models.CharField(default='classical', max_length=200),
            preserve_default=False,
        ),
    ]
