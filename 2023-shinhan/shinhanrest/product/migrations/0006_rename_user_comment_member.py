# Generated by Django 4.1.5 on 2023-01-20 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_delete_comment2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='member',
        ),
    ]
