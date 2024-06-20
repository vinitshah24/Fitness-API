from django.urls import path
from v2.workouts.urls import urlpatterns as workout_urls

app_name = "v2"

urlpatterns = []
urlpatterns.extend(workout_urls)
