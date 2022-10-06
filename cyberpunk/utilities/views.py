from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.template import loader

from utilities.models import Utility


def index(request):
    utilities = Utility.objects.all()
    context = {'utilities': utilities}
    return render(request, 'utilities/index.html', context)


def detail(request, utility_id):
    utility = get_object_or_404(Utility, pk=utility_id)
    return render(request, 'utilities/detail.html', {'utility': utility})
