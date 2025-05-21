import unittest
from aufgaben.a55_mitternachtsformel import calc_x1, calc_x2



class TestMitternachtsformel(unittest.TestCase):

    def test_zwei_loesungen(self):
        self.assertAlmostEqual(calc_x1(-2, 5, 3), -0.5)
        self.assertAlmostEqual(calc_x2(-2, 5, 3), 3.0)
        self.assertAlmostEqual(calc_x1(3, -14, 8), 4, places=4)
        self.assertAlmostEqual(calc_x2(3, -14, 8), 0.66666667, places=4)

    def test_eine_loesung(self):
        self.assertEqual(calc_x1(1, 2, 1), -1.0)
        self.assertEqual(calc_x2(1, 2, 1), -1.0)
        self.assertEqual(calc_x1(-4, -4, -1), -0.5)
        self.assertEqual(calc_x2(-4, -4, -1), -0.5)

    def test_keine_loesung(self):
        self.assertEqual(calc_x2(2, 2, 5), None)

        """
        with self.assertRaises(ValueError):
            calc_x1(2, 2, 5)
        with self.assertRaises(ValueError):
            calc_x2(2, 2, 5)
        with self.assertRaises(ValueError):
            calc_x1(-1, -2, -10)
        with self.assertRaises(ValueError):
            calc_x2(-1, -2, -10)
"""
if __name__ == '__main__':
    unittest.main()
