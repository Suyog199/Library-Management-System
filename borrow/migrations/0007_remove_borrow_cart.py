# Generated by Django 2.0 on 2019-05-25 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0006_auto_20190525_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='cart',
        ),
    ]
