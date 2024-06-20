from rest_framework import routers
from .views import WorkoutViewSet
from django.urls import path, include, re_path



app_name = "workouts"

router = routers.SimpleRouter()
router.register("", WorkoutViewSet, basename="workouts")
# urlpatterns = router.urls

urlpatterns = [
    path("workouts", include((router.urls, app_name), namespace='workouts')),
]