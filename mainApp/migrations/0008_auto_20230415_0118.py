# Generated by Django 3.2 on 2023-04-14 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_check_up_reservoir_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservoir',
            name='depth',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='length',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='water_level',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='width',
            field=models.FloatField(default=0),
        ),
    ]
