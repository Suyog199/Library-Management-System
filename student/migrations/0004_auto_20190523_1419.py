# Generated by Django 2.0 on 2019-05-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190523_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fullname',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=2, max_length=20),
        ),
    ]
