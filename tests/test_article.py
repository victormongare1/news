import unittest
from app.models import ARTICLE
class ArticleTest(unittest.TestCase):
  '''
  test class to test behaviour of the article class
  '''
  def setUp(self):
    '''
    setup method that will run before every test
    '''
    self.newarticle=ARTICLE("mike","news today","today","content")
  def test_instance(self):
    '''
    test to assert whether newsource is an instance of the source object
    '''
    self.assertTrue(isinstance(self.newarticle,ARTICLE))