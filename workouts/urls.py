from rest_framework import routers
from .views import WorkoutViewSet

app_name = "workouts"

router = routers.SimpleRouter()
router.register("", WorkoutViewSet, basename="workouts")
urlpatterns = router.urls
