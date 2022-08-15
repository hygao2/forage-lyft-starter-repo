import unittest

from tires.carrigan import CarriganTire
from tires.octoprime import OctoprimeTire


class TestTires(unittest.TestCase):
    def test_carrigan_needs_service_true(self):
        tire_wear = [0.8, 0.4, 0.9]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_needs_service_false(self):
        tire_wear = [0.7, 0.7, 0.6, 0.2]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())

    def test_octoprime_needs_service_true(self):
        tire_wear = [2, 0.7, 0.6, 0.2]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_octoprime_needs_service_false(self):
        tire_wear = [0.2, 0.7, 0.2]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())