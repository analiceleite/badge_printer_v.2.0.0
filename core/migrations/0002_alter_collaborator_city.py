# Generated by Django 5.0.8 on 2024-08-28 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
