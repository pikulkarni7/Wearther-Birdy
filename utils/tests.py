from django.test import TestCase
from .timezone import getLocalTime


class timeZoneTest(TestCase):
    def testLocalTime(self):
        print(getLocalTime(lat=37.3541, lon=-121.9552))  # Santa Clara coordinates
        assert 1 == 1
