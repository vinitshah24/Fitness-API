from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class WorkoutTestCase(TestCase):

    def setUp(self) -> None:
        self.workout_url_v2 = reverse("v2:workouts")

    def test_workout_url(self):
        print(self.workout_url_v2)
