# Generated by Django 5.0.6 on 2024-05-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.FloatField(default=10.0)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='images/products/photo')),
                ('discounts', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('is_available', models.BooleanField(default=False)),
                ('raiting', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
