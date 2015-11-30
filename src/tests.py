# -*- coding: utf-8 -*-

from unittest import TestCase

from geoip import get_location


class TestGeoIPService(TestCase):
    def setUp(self):
        self.ipv4 = {"136.39.103.199": "Dearborn",
                     "113.106.129.229": "Guangzhou",
                     "146.40.46.177": "San Ramon",
                     "132.125.225.179": "Sierra Vista",
                     "150.158.81.32": "Kortrijk",
                     "197.183.230.56": "Nairobi",
                     "34.105.31.180": "Houston",
                     "145.76.102.22": "Enschede",
                     "201.73.201.226": "Teixeira"}

    def test_get_location(self):
        for ip, location in self.ipv4.items():
            self.assertEqual(str(get_location('en', ip)["city"]["name"]),
                             location)