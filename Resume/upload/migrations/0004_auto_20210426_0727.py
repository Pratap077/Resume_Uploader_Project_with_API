# Generated by Django 3.1.6 on 2021-04-26 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20210423_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='my_file',
            field=models.FileField(upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(upload_to='profileimg'),
        ),
    ]
