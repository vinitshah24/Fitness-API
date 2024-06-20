from django.test import TestCase
from django.shortcuts import reverse
from django.conf import settings
from django.urls import URLPattern, URLResolver

class WorkoutTestCase(TestCase):

    def setUp(self) -> None:
        self.workout_url_v1 = reverse("v1:workouts-list")

    def test_workout_url(self):
        print(self.workout_url_v1)

    # def test_get_url_list(self):
    #     def list_urls(lis, acc=None):
    #         if acc is None:
    #             acc = []
    #         if not lis:
    #             return
    #         l = lis[0]
    #         if isinstance(l, URLPattern):
    #             yield acc + [str(l.pattern)]
    #         elif isinstance(l, URLResolver):
    #             yield from list_urls(l.url_patterns, acc + [str(l.pattern)])
    #         yield from list_urls(lis[1:], acc)

    #     urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])
    #     for p in list_urls(urlconf.urlpatterns):
    #         print(''.join(p))
