from random import random
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

class Ability(models.Model):
    name = models.CharField(max_length=15)
    abbreviation = models.CharField(max_length=3, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Abilities"

class Skill(models.Model):
    name = models.CharField(max_length=25)
    abbreviation = models.CharField(max_length=5, blank=True, null=True)
    description = models.TextField(blank=True)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class WeaponType(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type

class ArmorType(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type

class ToolType(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return self.type

class language(models.Model):
    name  = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Dice(models.Model):
    sides = models.IntegerField()

    def __str__(self):
        return 'd' + str(self.sides)

    def role_dice(self, nr_of_dice):
        result = 0
        for d in range(0, nr_of_dice):
            result += random.randint(1, self.sides)

        return result

class Feature(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = RichTextField(blank=True)
    classFeature = models.BooleanField()

    # modifiers = 
    # spells = 
    # actions = 

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = RichTextField(blank=True)
    short_description = RichTextField(blank=True)
    quick_build = RichTextField(blank=True)

    primary_ability = models.ForeignKey(Ability, related_name='class_primary_ability', on_delete=models.SET_NULL, null=True, blank=True)
    hit_die = models.ForeignKey(Dice, on_delete=models.SET_NULL, null=True, blank=True)
    armor_proficiency = models.ManyToManyField(ArmorType)
    weapon_proficiency = models.ManyToManyField(WeaponType)
    tool_proficiency = models.ManyToManyField(ToolType)
    saves = models.ManyToManyField(Ability, related_name='class_saves')
    skills = models.ManyToManyField(Skill)

    class_spesific_features = ArrayField(models.CharField(max_length=25), null=True, blank=True)
    spell_slot_levels = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    sub_class_name = models.CharField(max_length=25, blank=True)
    sub_class_description = models.TextField(blank=True)

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Classes"

class SubClass(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True)
    cls = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Sub classes"

class ClassLevel(models.Model):
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    cls = models.ForeignKey(Class, on_delete=models.CASCADE)
    proficiency_bonus = models.IntegerField()
    class_feature = models.ManyToManyField(Feature, blank=True)
    class_spesific = ArrayField(models.CharField(max_length=15), null=True)
    spell_slots = ArrayField(models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)]), size=9, null=True)

    def __str__(self):
        return f"{self.level}: {self.cls}"

class SubClassLevel(models.Model):
    sub_class = models.ForeignKey(SubClass, on_delete=models.CASCADE)
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)
    class_feature = models.ManyToManyField(Feature)

    def __str__(self):
        return f"{self.class_level.level}: {self.sub_class}"

