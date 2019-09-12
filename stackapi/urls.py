from django.urls import path, include
from .views import index, latest
from rest_framework import routers




urlpatterns = [
    path('', index, name="index"),
    path('api/', include('stackapi.api.urls')),
    path('latest/', latest, name="latest"),
]
