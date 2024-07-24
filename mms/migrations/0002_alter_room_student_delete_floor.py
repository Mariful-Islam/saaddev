# Generated by Django 5.0.6 on 2024-07-23 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mms.student'),
        ),
        migrations.DeleteModel(
            name='Floor',
        ),
    ]