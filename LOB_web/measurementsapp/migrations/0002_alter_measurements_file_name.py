# Generated by Django 3.2.3 on 2021-06-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurementsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='file_name',
            field=models.FileField(null=True, upload_to='main_web/documents/Measurements/'),
        ),
    ]