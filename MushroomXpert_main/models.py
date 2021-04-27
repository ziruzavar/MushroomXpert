from django.db import models


class FindMushroom(models.Model):
    image = models.ImageField(upload_to='Ai_images')


class Mushroom(models.Model):
    EDIBLE = 'ED'
    POISONOUS = 'PO'
    NOT_EDIBLE = 'NE'

    EDIBLE_CHOICES = [
        (EDIBLE, 'Edible'),
        (POISONOUS, 'Poisonous'),
        (NOT_EDIBLE, 'Not edible'),
    ]

    name = models.CharField(max_length=30, default='none', primary_key=True)
    description = models.TextField(default='none')
    image_url = models.URLField(default='none')
    edible_choices = models.CharField(max_length=2, choices=EDIBLE_CHOICES, default=NOT_EDIBLE)
