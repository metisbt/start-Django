# Generated by Django 3.2.23 on 2024-02-05 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contact_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='sbject',
            new_name='subject',
        ),
    ]
