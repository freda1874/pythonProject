from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.post)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b1 = Blog('Test', 'Test Author')
        b1.post = ['Test']
        b2 = Blog('Test', 'Test Author')
        b2.post = ['Test', 'Test2']

        self.assertEqual(b.__repr__(), 'Test by Test Author(0 post)')
        self.assertEqual(b1.__repr__(), 'Test by Test Author(1 post)')
        self.assertEqual(b2.__repr__(), 'Test by Test Author(2 posts)')


