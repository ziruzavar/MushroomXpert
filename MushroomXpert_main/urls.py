from django.urls import path

from MushroomXpert_main.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index")
]
