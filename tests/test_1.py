import unittest


class Test1(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOOx')


if __name__ == '__main__':
    unittest.main()
