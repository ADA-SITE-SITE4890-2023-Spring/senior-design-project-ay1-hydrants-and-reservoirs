# Generated by Django 3.2 on 2023-04-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_up_reservoir',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
