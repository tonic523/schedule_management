# Generated by Django 3.2.4 on 2021-06-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_annual_vacation_user_annual_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='remaining_annual_leave',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
