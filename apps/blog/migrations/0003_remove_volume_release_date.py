# Generated by Django 5.1.3 on 2024-12-10 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_volume_alter_blogpost_volume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volume',
            name='release_date',
        ),
    ]