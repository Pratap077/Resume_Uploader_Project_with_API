# Generated by Django 3.1.6 on 2021-04-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20210426_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='my_file',
            field=models.FileField(blank=True, upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profileimg'),
        ),
    ]
