# Generated by Django 2.0 on 2019-05-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0009_auto_20190525_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
