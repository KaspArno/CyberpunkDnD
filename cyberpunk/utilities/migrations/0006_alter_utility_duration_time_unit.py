# Generated by Django 4.1.1 on 2022-10-04 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0005_utility_at_higher_levels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='duration_time_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilities.durationtimeunit'),
        ),
    ]
