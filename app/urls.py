from django.contrib import admin
from django.urls import path, include

base_path = "api"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{base_path}/v1/", include("v1.urls", namespace="v1"), name="v1"),
    path(f"{base_path}/v2/", include("v2.urls", namespace="v2"), name="v2"),
]
