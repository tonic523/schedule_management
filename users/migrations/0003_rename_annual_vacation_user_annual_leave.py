# Generated by Django 3.2.4 on 2021-06-15 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210614_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='annual_vacation',
            new_name='annual_leave',
        ),
    ]