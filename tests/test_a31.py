import unittest
from aufgaben.a31_waehrungsumrechner import euro_to_usd


class TestEuroToUSD(unittest.TestCase):
    def test_a(self):
        self.assertAlmostEqual(euro_to_usd(10), 11.163, places=3)
        self.assertAlmostEqual(euro_to_usd(12.34), 13.775142, places=3)
        self.assertAlmostEqual(euro_to_usd(50), 55.815, places=3)
        self.assertAlmostEqual(euro_to_usd(99.99), 111.618837, places=3)
        self.assertAlmostEqual(euro_to_usd(1.11), 1.239093, places=3)
        self.assertAlmostEqual(euro_to_usd(25.75), 28.744725, places=3)
        self.assertAlmostEqual(euro_to_usd(0.01), 0.011163, places=3)
        self.assertAlmostEqual(euro_to_usd(200), 223.26, places=3)
        self.assertAlmostEqual(euro_to_usd(5.5), 6.13965, places=3)
        self.assertAlmostEqual(euro_to_usd(1000), 1116.3, places=3)