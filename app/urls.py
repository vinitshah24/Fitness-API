from django.contrib import admin
from django.urls import path, include

base_path = "api"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{base_path}/v1/workouts/", include("workouts.urls", namespace="v1"))
]
