from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView

import json

from rest_framework import viewsets

from MushroomXpert_main.forms import MushroomForm
from Ai_logic.weights_loader import pred, model
from MushroomXpert_main.models import Mushroom
from MushroomXpert_main.serializers import MushroomSerializer


class IndexView(View):
    def get(self, request, **kwargs):
        form = MushroomForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request, **kwargs):
        form = MushroomForm(request.POST, request.FILES)
        if form.is_valid():
            index = pred.feed_image(form.cleaned_data['image'], model)
            f = open('Ai_logic/classes.json')
            labels = json.load(f)
            print(index)
            context = {'first': labels[str(index[0])], 'index': index[0]}
            f.close()
            return redirect(f'/?shroom={context["first"]}')
        else:
            form = MushroomForm()
            return render(request, 'index.html', {'form': form})


class AboutView(TemplateView):
    template_name = './about.html'


class MushroomsView(ListView):
    template_name = './mushrooms.html'
    model = Mushroom

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mushrooms'] = Mushroom.objects.all()
        return context


class MushroomViewSet(viewsets.ModelViewSet):
    queryset = Mushroom.objects.all()
    serializer_class = MushroomSerializer

