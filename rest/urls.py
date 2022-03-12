from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from django.conf.urls import url, include

from originsite.urls import router as originsite_router

# PRIVATE_DIR = getattr(settings, 'STATIC_URL', None)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path("api/", include(ecsite_router.urls)),
    path("api/", include("originsite.urls")),
]
