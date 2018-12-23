# Generated by Django 2.1.3 on 2018-11-27 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Register_App', '0007_auto_20181124_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participants',
            old_name='name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='rating',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='title',
            new_name='teamName',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='EmployeeID',
        ),
        migrations.RemoveField(
            model_name='participants',
            name='phone',
        ),
        migrations.AddField(
            model_name='team',
            name='High_Level_Design',
            field=models.TextField(default='@'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='benefits',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='detailed_design',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.CharField(default='abc@gmail.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='has_idea_implemented_anywhere',
            field=models.TextField(default='yes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='idea_detail',
            field=models.TextField(default='this is not implemented anywhere'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='solution_platform',
            field=models.TextField(default='no solution yet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='theme',
            field=models.CharField(choices=[('Prevention', 'Prevention'), ('Detection', 'Detection'), ('Resolution', 'Resolution'), ('UserInterface', 'UserInterface'), ('Commercial', 'Commercial'), ('DeliveryModel', 'DeliveryModel')], default='Commercial', max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='title_desc',
            field=models.CharField(default='no title described', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='usd_Cost_To_Implement',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='usd_benefits_perannum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]