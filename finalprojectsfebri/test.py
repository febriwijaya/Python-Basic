import unittest
from directors import *
from app import connex_app

class TestDirectors(unittest.TestCase):

  def test_read_all(self):
    self.assertIs(type(read_all()), list)

  def test_read_one(self):
    self.assertIs(type(read_one(4770)), dict)

class FlaskTestCase(unittest.TestCase):
  def test_get_all_directors(self):
    connex_app.app.testing = True
    tester = connex_app.app.test_client(self)
    response = tester.get('/api/directors')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
