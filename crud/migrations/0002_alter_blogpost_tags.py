# Generated by Django 3.2.25 on 2024-08-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(max_length=100),
        ),
    ]
