from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader
from django.views import generic

from utilities.models import Test, Utility
from utilities.filters import UtilityFilter


class UtilityListView(generic.ListView):
    template_name = 'utilities/index.html'
    context_object_name = 'utilities'
    # listing_filters = UtilityFilter(request.GET, queryset=Utility.objects.all())

    def get_queryset(self):
        """Return all untilities."""
        return Utility.objects.order_by('name')


class UtilityDetailView(generic.DetailView):
    model = Utility
    template_name = 'utilities/detail.html'

def utility_list(request):
    utilities = Utility.objects.all()
    utilities_filter = UtilityFilter(request.GET, queryset=utilities)
    context = {
        'utilities_filter': utilities_filter
    }
    return render(request, "utilities/utility_list.html", context)

class TestDetailView(generic.DetailView):
    model = Test