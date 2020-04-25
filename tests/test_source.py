import unittest
from app.models import SOURCE
class SourceTest(unittest.TestCase):
  '''
  test class to test behaviour of the movie class
  '''
  def setUp(self):
    '''
    setup method that will run before every test
    '''
    self.newsource=SOURCE("abc-news","ABC-NEWS","trusted news source",
    "https://news","general")
  def test_instance(self):
    '''
    test to assert whether newsource is an instance of the source object
    '''
    self.assertTrue(isinstance(self.newsource,SOURCE))