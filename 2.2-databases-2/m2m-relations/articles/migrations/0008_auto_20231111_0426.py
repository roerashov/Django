# Generated by Django 2.2.9 on 2023-11-11 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20231111_0357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scope',
            new_name='scopes',
        ),
    ]
