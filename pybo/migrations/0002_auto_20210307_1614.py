# Generated by Django 3.1.5 on 2021-03-07 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='create_data',
            new_name='create_date',
        ),
    ]
