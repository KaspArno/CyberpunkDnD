from django.contrib import admin
from .models import Class, SubClass, ClassLevel, SubClassLevel, Feature, Dice, Ability, Skill, ArmorType, WeaponType, ToolType

class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Class Information', {'fields': ['name', 'description', 'short_description', 'quick_build', 'spell_slot_levels', 'sub_class_name', 'sub_class_description']}),
        ('Class Proficiencyes', {'fields': ['armor_proficiency', 'weapon_proficiency', 'tool_proficiency', 'saves', 'skills']}),
        ('Class Features', {'fields': ['primary_ability', 'hit_die', 'class_spesific_features']})
    ]
    list_display = ('name', 'short_description')
    list_filter = ['name', 'primary_ability', 'hit_die', 'saves', 'sub_class_name']
    search_fields = ['name']

class SubClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'cls', 'description')
    list_filter = ['name', 'cls']
    search_fields = ['name', 'cls']

class ClassLevelAdmin(admin.ModelAdmin):
    list_display = ('level', 'cls', 'proficiency_bonus')
    list_filter = ['level', 'cls']
    search_fields = ['level', 'cls']

class SubClassLevelAdmin(admin.ModelAdmin):
    list_filter = ['class_level', 'sub_class']

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Class, ClassAdmin)
admin.site.register(SubClass, SubClassAdmin)
admin.site.register(ClassLevel, ClassLevelAdmin)
admin.site.register(SubClassLevel, SubClassLevelAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Dice)
admin.site.register(Ability)
admin.site.register(Skill)
admin.site.register(ArmorType)
admin.site.register(WeaponType)
admin.site.register(ToolType)