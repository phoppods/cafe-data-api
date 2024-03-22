# Generated by Django 5.0.3 on 2024-03-13 14:43

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_task_delete_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField(unique=True)),
                ('store_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
           
        ),
    ]
