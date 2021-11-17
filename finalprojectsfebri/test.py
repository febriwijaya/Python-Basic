import unittest

from directors import read_all
from movies import read_all

class TestDirectors(unittest.TestCase):

    def test_read_all(self):
        self.assertIs(type(read_all()), list)

class TestMovies(unittest.TestCase):
  
    def test_read_all(self):
        self.assertIs(type(read_all()), list)


if __name__ == '__main__':
    unittest.main()