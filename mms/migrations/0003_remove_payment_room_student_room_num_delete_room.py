# Generated by Django 5.0.6 on 2024-07-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mms', '0002_alter_room_student_delete_floor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='room',
        ),
        migrations.AddField(
            model_name='student',
            name='room_num',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
