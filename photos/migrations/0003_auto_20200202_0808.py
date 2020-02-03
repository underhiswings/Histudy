# Generated by Django 3.0.2 on 2020-02-02 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
