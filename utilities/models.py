from email.policy import default
from re import A
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class SchoolsOfMagic(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Schools of Magic'


class UtilityComponent(models.Model):
    abbreviation = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=15)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UtilityLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.CharField(max_length=10)

    def __str__(self):
        return self.level


class UtilityCastingTimeUnit(models.Model):
    unit = models.CharField(max_length=15)

    def __str__(self):
        return self.unit


class RangeType(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type

class RangeUnit(models.Model):
    unit = models.CharField(max_length=10)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.unit

class AreaType(models.Model):
    type = models.CharField(max_length=10)

    def __str__(self):
        return self.type


class DurationType(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class DurationTimeUnit(models.Model):
    unit = models.CharField(max_length=10)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.unit


class Utility(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = RichTextField(blank=True)
    # description = models.TextField(blank=True)
    at_higher_levels = RichTextField(blank=True)
    # at_higher_levels = models.TextField(blank=True)
    ritual = models.BooleanField(default=False)
    utility_level = models.ForeignKey(
        UtilityLevel, models.SET_DEFAULT, default=0)
    casting_time_unit = models.ForeignKey(
        UtilityCastingTimeUnit, models.SET_DEFAULT, default=1)
    casting_time_quantity = models.IntegerField(null=True, default=1)
    reaction_casting_description = models.TextField(blank=True)
    components = models.ManyToManyField(UtilityComponent, blank=True)
    material_components = models.TextField(blank=True)

    range_type = models.ForeignKey(RangeType, models.SET_NULL, null=True)
    range_distance = models.IntegerField(null=True, default=0)
    range_unit = models.ForeignKey(RangeUnit, related_name='untility_range', on_delete=models.SET_NULL, null=True, blank=True)
    aoe = models.ForeignKey(AreaType, on_delete=models.SET_NULL, null=True, blank=True)
    aoe_unit = models.ForeignKey(RangeUnit, related_name='untility_aoe', on_delete=models.SET_NULL, null=True, blank=True)
    aoe_unit_quantity = models.IntegerField(null=True, blank=True)
    
    duration_type = models.ForeignKey(DurationType, models.SET_NULL, null=True)
    duration_time_unit = models.ForeignKey(
        DurationTimeUnit, on_delete=models.SET_NULL, null=True, blank=True)
    duration_quantity = models.IntegerField(null=True, blank=True)
    origin = models.CharField(max_length=25, blank=True)
    origin_link = models.URLField(blank=True)

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Utilities'