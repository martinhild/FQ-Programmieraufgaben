import unittest

from aufgaben.a66_umwandlung_sekunden import calc

class TestCalc(unittest.TestCase):
    def test_testTrue(self):
        self.assertEqual(calc(7200),  (2, 0, 0))
        self.assertEqual(calc(3661),  (1, 1, 1))
        self.assertEqual(calc(0),     (0, 0, 0))
        self.assertEqual(calc(59),    (0, 0,59))

    def test_testFalse(self):
        self.assertNotEqual(calc(7200), (1,59,59))
        self.assertNotEqual(calc(3601), (0, 60,1))
        self.assertNotEqual(calc(61),   (0, 1, 2))
        self.assertNotEqual(calc(0),    (1, 0, 0))

if __name__ == "__main__":
    unittest.main()