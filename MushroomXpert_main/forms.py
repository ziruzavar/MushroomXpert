from django import forms

from MushroomXpert_main.models import FindMushroom


class MushroomForm(forms.ModelForm):
    class Meta:
        model = FindMushroom
        fields = ('image',)
