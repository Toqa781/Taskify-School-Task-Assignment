# Generated by Django 5.0.6 on 2024-05-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_alter_task_options_alter_task_taskiid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Taskiid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='admin',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='teacher',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
