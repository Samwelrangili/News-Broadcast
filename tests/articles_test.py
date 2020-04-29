import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):
    '''
    Class to test the behaviour of the articles class
    '''
    def setUp(self):
        self.new_article = Articles('H.Z Jones', 'Pandemic', 'Covid-19 crisis', 'https://bing.com', 'https://bing.com/images', '2019-10-12T11:31:03Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_article.author, 'H.Z Jones')
        self.assertEquals(self.new_article.title, 'Pandemic')
        self.assertEquals(self.new_article.description, 'Covid-19 crisis')
        self.assertEquals(self.new_article.url, 'https://bing.com')
        self.assertEquals(self.new_article.urlToImage,'https://bing.com/images')
        self.assertEquals(self.new_article.publishedAt, '2019-10-12T11:31:03Z')