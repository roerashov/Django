# Generated by Django 2.2.9 on 2023-11-11 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20231109_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scopes',
            old_name='Tag',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='scopes',
            old_name='Article',
            new_name='title',
        ),
    ]