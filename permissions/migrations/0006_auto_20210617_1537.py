# Generated by Django 3.2.4 on 2021-06-17 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0005_alter_userrole_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='description',
        ),
        migrations.AddField(
            model_name='role',
            name='type',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]
