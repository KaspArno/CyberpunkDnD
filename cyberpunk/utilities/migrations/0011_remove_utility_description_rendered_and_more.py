# Generated by Django 4.1.2 on 2022-10-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0010_alter_utility_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utility',
            name='description_rendered',
        ),
        migrations.AlterField(
            model_name='utility',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
