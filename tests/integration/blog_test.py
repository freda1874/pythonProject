from unittest import TestCase

import blog
from blog import Blog


class BlogTest(TestCase):

    def test_create_post_in_blog(self):
        b1 = Blog('Test', 'Test Author')
        b1.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b1.post), 1)

        self.assertEqual(b1.post[0].title, 'Test Post')
        self.assertEqual(b1.post[0].content, 'Test Content')

    def test_jason(self):
        b1 = Blog('Test', 'Test Author')
        b1.create_post('Test Post', 'Test Content')

        expected = {'title': 'Test', 'author': 'Test Author',
                    'post': [{'title': 'Test Post', 'content': 'Test Content'}]}

        self.assertDictEqual(expected, b1.json())
