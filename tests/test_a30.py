import unittest
from aufgaben.a_030_isbn_pruefung import _check_isbn

class TestCheckISBN(unittest.TestCase):
    def test_check_isbn(self):
        # correct ISBN-10
        self.assertTrue(_check_isbn("0-306-40615-2"))
        self.assertTrue(_check_isbn("0-306-40615-2"))
        self.assertTrue(_check_isbn("0306406152"))
        self.assertTrue(_check_isbn("123456789X"))

        # incorrect ISBN-10
        self.assertFalse(_check_isbn("1234567890"))
        self.assertFalse(_check_isbn("12345"))

        # correct ISBN-13
        self.assertTrue(_check_isbn("9780306406157"))

        # incorrect ISBN-13
        self.assertFalse(_check_isbn("978030640615822222"))
        self.assertFalse(_check_isbn("9780306406156"))


if __name__ == "__main__":
    unittest.main() # scannt nach Funktionen die mit test_ anfangen
