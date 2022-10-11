from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader
from django.views import generic

from utilities.models import Utility


class UtilityListView(generic.ListView):
    template_name = 'utilities/index.html'
    context_object_name = 'utilities'

    def get_queryset(self):
        """Return all untilities."""
        return Utility.objects.order_by('name')


class UtilityDetailView(generic.DetailView):
    model = Utility
    template_name = 'utilities/detail.html'
