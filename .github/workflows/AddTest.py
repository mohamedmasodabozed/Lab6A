import unittest


class Addition:
    def add(self, x, y):
        return x + y


class TestAdd(unittest.TestCase):
    def test_add(self):
        addition = Addition()
        self.assertEqual(addition.add(4, 3), 7)
        self.assertEqual(addition.add(2, 1), 3)
        self.assertEqual(addition.add(0, 0), 0)
