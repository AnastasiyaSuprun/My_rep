# Generated by Django 3.2.15 on 2023-02-01 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='owner_field',
            new_name='owner',
        ),
    ]