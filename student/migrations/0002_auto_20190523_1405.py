# Generated by Django 2.0 on 2019-05-23 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lname',
        ),
    ]