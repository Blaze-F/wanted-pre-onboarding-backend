# Generated by Django 4.1.2 on 2022-10-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preonboard', '0002_job_opening_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicate',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job_opening',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
