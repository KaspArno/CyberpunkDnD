# Generated by Django 4.1.1 on 2022-10-24 19:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0012_test2_alter_test_test_field_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Test2',
        ),
        migrations.AlterField(
            model_name='utility',
            name='at_higher_levels',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='utility',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
