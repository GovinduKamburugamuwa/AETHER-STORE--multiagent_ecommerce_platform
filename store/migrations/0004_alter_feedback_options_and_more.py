# Generated by Django 5.1.4 on 2024-12-23 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_feedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={},
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='user',
        ),
    ]
