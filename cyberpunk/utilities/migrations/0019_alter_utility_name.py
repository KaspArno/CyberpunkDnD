# Generated by Django 4.1.1 on 2022-10-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0018_areatype_utility_aoe_unit_utility_aoe_unit_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
