# Generated by Django 2.0 on 2019-05-28 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20190527_2209'),
        ('borrow', '0011_auto_20190527_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='Book',
        ),
        migrations.AddField(
            model_name='borrow',
            name='Book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.Book'),
        ),
    ]
