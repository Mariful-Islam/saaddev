# Generated by Django 5.0.6 on 2024-07-19 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_user_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
