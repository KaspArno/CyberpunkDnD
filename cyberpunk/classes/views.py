from django.shortcuts import render
from django.views import generic
from .models import Class, ClassLevel


class ClassListView(generic.ListView):
    model = Class
    context_object_name = 'classes'

class ClassDetailView(generic.DetailView):
    model = Class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['levels'] = Class.classlevel_set.all()
        levels = ClassLevel.objects.filter(cls=self.object).prefetch_related('class_feature')
        features = set()
        for level in levels:
            features.update(level.class_feature.all())
        saving_thows = set()
        saving_thows.update(self.object.saves.all())
        armor_proficiencies = set()
        armor_proficiencies.update(self.object.armor_proficiency.all())
        weapon_proficiencies = set()
        weapon_proficiencies.update(self.object.weapon_proficiency.all())
        context['levels'] = levels
        context['features'] = features
        context['saves'] = saving_thows
        context['armor_proficiencies'] = armor_proficiencies
        context['weapon_proficiencies'] = weapon_proficiencies
        return context