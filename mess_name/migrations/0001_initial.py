# Generated by Django 5.0 on 2024-03-05 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_name', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('owner', models.CharField(max_length=100)),
                ('owner_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]
