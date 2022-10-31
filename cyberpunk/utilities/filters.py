import django
import django_filters
from utilities.models import Utility

class UtilityFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        super(UtilityFilter, self).__init__(*args, **kwargs)
        self.form.initial['archive'] = False


    class Meta:
        model = Utility
        fields = {'name': ['icontains'], 'utility_level': ['exact'], 'origin': ['icontains']}