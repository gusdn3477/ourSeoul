# Generated by Django 3.1.5 on 2021-03-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_question_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]