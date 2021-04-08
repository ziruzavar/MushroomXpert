from django.db import models


class Mushroom(models.Model):
    image = models.ImageField(upload_to='Ai_images')
