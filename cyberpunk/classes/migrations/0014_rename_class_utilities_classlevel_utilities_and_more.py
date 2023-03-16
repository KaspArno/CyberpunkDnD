# Generated by Django 4.1.2 on 2023-03-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0021_alter_utility_slug'),
        ('classes', '0013_rename_utiliy_slots_classlevel_utility_slots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classlevel',
            old_name='class_utilities',
            new_name='utilities',
        ),
        migrations.AddField(
            model_name='class',
            name='class_utilities',
            field=models.ManyToManyField(blank=True, to='utilities.utility'),
        ),
        migrations.AddField(
            model_name='subclasslevel',
            name='utilities',
            field=models.ManyToManyField(blank=True, to='utilities.utility'),
        ),
    ]
