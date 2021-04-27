from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from MushroomXpert_main.views import IndexView, AboutView, MushroomsView, MushroomViewSet

from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'mushroom', MushroomViewSet)
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name='about'),
    path('mushrooms', MushroomsView.as_view(), name='mushrooms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
