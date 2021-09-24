# Generated by Django 3.1.3 on 2021-09-24 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjectsapp', '0010_auto_20210813_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_record',
            name='comorbidities_ids',
            field=models.ManyToManyField(blank=True, null=True, related_name='comorbidities', to='subjectsapp.Comorbidities'),
        ),
        migrations.AlterField(
            model_name='medical_record',
            name='diseases_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diseases', to='subjectsapp.diseases'),
        ),
    ]
