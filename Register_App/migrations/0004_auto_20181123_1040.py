# Generated by Django 2.1.3 on 2018-11-23 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register_App', '0003_remove_participants_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participants',
            name='Team',
        ),
        migrations.DeleteModel(
            name='Participants',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]