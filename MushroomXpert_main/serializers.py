from rest_framework import serializers
from MushroomXpert_main.models import Mushroom


class MushroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mushroom
        fields = ('name', 'description', 'image_url', 'edible_choices')
