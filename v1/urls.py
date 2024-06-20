from django.urls import path
from v1.workouts.urls import urlpatterns as workout_urls  # import views from v1.workout
from django.urls import path, include, re_path

app_name = "v1"

urlpatterns = workout_urls

# urlpatterns = [
#     path("workouts/", include((workout_urls, app_name))),
# ]