# Generated by Django 4.1.2 on 2022-10-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preonboard', '0006_remove_job_opening_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
