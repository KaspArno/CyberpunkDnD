# Generated by Django 4.1.1 on 2022-10-04 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0017_utility_casting_time_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utility',
            name='casting_time_type',
        ),
    ]
