# Generated by Django 4.0.1 on 2022-01-15 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drone_api', '0007_drone_medications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drone',
            name='medications',
        ),
        migrations.AddField(
            model_name='medication',
            name='drone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='drone_api.drone'),
        ),
    ]
