# Generated by Django 3.2.3 on 2021-06-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjectsapp', '0007_alter_medical_record_hc_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_record',
            name='HC_number',
            field=models.CharField(max_length=20),
        ),
    ]
