# Generated by Django 4.1.1 on 2022-10-04 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DurationTimeUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DurationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RangeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UtilityCastingTimeUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UtilityLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='utility',
            name='casting_time_quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='components',
            field=models.ManyToManyField(blank=True, to='utilities.utilitycomponent'),
        ),
        migrations.AddField(
            model_name='utility',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='duration_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='range_distance',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='reaction_casting_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='utility',
            name='ritual',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utility',
            name='casting_time_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='utilities.utilitycastingtimeunit'),
        ),
        migrations.AddField(
            model_name='utility',
            name='duration_time_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilities.durationtimeunit'),
        ),
        migrations.AddField(
            model_name='utility',
            name='duration_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilities.durationtype'),
        ),
        migrations.AddField(
            model_name='utility',
            name='range_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilities.rangetype'),
        ),
        migrations.AddField(
            model_name='utility',
            name='utility_level',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='utilities.utilitylevel'),
        ),
    ]
