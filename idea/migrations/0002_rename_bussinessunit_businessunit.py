# Generated by Django 4.1.4 on 2023-01-07 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_years_of_experience'),
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BussinessUnit',
            new_name='BusinessUnit',
        ),
    ]
