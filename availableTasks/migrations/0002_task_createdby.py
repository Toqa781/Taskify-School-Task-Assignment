# Generated by Django 5.0.6 on 2024-05-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('availableTasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='createdby',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
