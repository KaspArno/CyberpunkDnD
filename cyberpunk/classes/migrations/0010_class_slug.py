# Generated by Django 4.1.2 on 2023-03-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_class_sub_class_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
