# Generated by Django 5.0.6 on 2024-05-14 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tea_and_coffe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='raiting',
            new_name='rating',
        ),
    ]
