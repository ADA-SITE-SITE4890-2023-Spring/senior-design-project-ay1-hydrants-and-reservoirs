# Generated by Django 3.2 on 2023-04-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20230415_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_up_hydrant',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
