# Generated by Django 4.1.1 on 2022-10-23 18:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0009_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
