# Generated by Django 4.1.2 on 2023-03-12 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0020_utility_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]