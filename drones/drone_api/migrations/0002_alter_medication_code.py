# Generated by Django 4.0.1 on 2022-01-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='code',
            field=models.CharField(max_length=255),
        ),
    ]