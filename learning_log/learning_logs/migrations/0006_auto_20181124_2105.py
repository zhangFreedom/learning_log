# Generated by Django 2.1.2 on 2018-11-24 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_auto_20181122_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img',
            old_name='pic',
            new_name='img',
        ),
    ]