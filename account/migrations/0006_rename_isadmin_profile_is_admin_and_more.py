# Generated by Django 4.1.4 on 2023-01-08 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_years_of_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='isAdmin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='isJury',
            new_name='is_jury',
        ),
    ]
