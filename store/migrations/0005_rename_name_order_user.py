# Generated by Django 4.2.1 on 2023-05-20 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='user',
        ),
    ]
