# Generated by Django 2.0 on 2019-06-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0019_auto_20190603_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
