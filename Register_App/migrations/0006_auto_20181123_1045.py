# Generated by Django 2.1.3 on 2018-11-23 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register_App', '0005_auto_20181123_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='title_name',
            new_name='title',
        ),
    ]
