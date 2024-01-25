from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("components/hero.html", hero, name="hero"),
    path("components/about.html", about, name="about"),
]
