# Generated by Django 3.2.23 on 2024-01-28 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_updated_time_post_updated_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date']},
        ),
    ]
