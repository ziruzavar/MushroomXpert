from django import forms

from MushroomXpert_main.models import Mushroom


class MushroomForm(forms.ModelForm):
    class Meta:
        model = Mushroom
        fields = ('image',)
