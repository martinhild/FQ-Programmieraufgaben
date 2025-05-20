import unittest
from aufgaben.a39_gespiegelte_zeichen_ausgabe import mirror_word

class TestMirrorWord(unittest.TestCase):

    def test_lower_case(self):
        self.assertEqual("z", mirror_word("a"))
        self.assertEqual("zyx", mirror_word("abc"))
        self.assertEqual("svool", mirror_word("hello"))

    def test_upper_case(self):
        self.assertEqual("Z", mirror_word("A"))
        self.assertEqual("ZYX", mirror_word("ABC"))
        self.assertEqual("DLIOW", mirror_word("WORLD")) # Zahlen bleiben gleich

    def test_no_letters(self):
        self.assertEqual("123!?", mirror_word("123!?"))
        self.assertEqual("!@#$%", mirror_word("!@#$%"))

    def test_mixed(self):
        self.assertEqual("ZyX", mirror_word("AbC"))
        self.assertEqual("Gvhg123", mirror_word("Test123"))

if __name__ == "__main__":
    unittest.main()
