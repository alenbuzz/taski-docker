# Generated by Django 3.2.16 on 2023-09-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Title'),
        ),
    ]
