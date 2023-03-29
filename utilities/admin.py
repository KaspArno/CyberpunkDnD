from django.contrib import admin

from utilities.models import AreaType, DurationTimeUnit, DurationType, RangeType, RangeUnit, SchoolsOfMagic, Utility, UtilityCastingTimeUnit, UtilityComponent, UtilityLevel

# admin.site.register(Utility)


class UtilityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'at_higher_levels',
         'utility_level', 'ritual', 'components', 'material_components']}),
        ('Castiong Time', {'fields': [
         'casting_time_quantity', 'casting_time_unit', 'reaction_casting_description']}),
        ('Range', {'fields': ['range_type', 'range_distance', 'range_unit', 'aoe', 'aoe_unit', 'aoe_unit_quantity']}),
        ('Duration', {'fields': ['duration_type',
         'duration_quantity', 'duration_time_unit']}),
        ('Origin', {'fields': ['origin', 'origin_link']}),
    ]
    list_display = ('name', 'utility_level')
    list_filter = ['utility_level', 'ritual', 'range_type', 'duration_type']
    search_fields = ['name', 'description', 'at_higher_levels']


admin.site.register(Utility, UtilityAdmin)
admin.site.register(RangeUnit)
admin.site.register(DurationTimeUnit)
admin.site.register(AreaType)
