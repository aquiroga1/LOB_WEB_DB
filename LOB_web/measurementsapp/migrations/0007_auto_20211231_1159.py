# Generated by Django 3.1.3 on 2021-12-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurementsapp', '0006_auto_20210927_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='file_name',
            field=models.FileField(blank=True, null=True, upload_to='main_web/media/Measurements/'),
        ),
    ]