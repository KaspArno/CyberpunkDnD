from django.contrib import admin

from utilities.models import DurationTimeUnit, DurationType, RangeType, SchoolsOfMagic, Utility, UtilityCastingTimeUnit, UtilityComponent, UtilityLevel

admin.site.register(Utility)
admin.site.register(UtilityLevel)
admin.site.register(UtilityCastingTimeUnit)
admin.site.register(RangeType)
admin.site.register(DurationTimeUnit)
admin.site.register(DurationType)
admin.site.register(UtilityComponent)
