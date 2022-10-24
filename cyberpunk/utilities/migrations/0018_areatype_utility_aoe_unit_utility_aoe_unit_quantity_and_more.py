# Generated by Django 4.1.1 on 2022-10-24 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0017_alter_utility_casting_time_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='utility',
            name='aoe_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='untility_aoe', to='utilities.rangeunit'),
        ),
        migrations.AddField(
            model_name='utility',
            name='aoe_unit_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rangeunit',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='utility',
            name='range_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='untility_range', to='utilities.rangeunit'),
        ),
        migrations.AddField(
            model_name='utility',
            name='aoe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilities.areatype'),
        ),
    ]
