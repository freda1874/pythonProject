from unittest import TestCase
from unittest.mock import patch

import app
import blog
from blog import Blog
from post import Post

# Test class for the app module
class AppTest(TestCase):

    # Set up function to create a test blog before each test
    def setUp(self):
        blog_name = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog_name}

    # Test to ensure the menu prints the correct prompt
    def test_menu_prints_promt(self):
        with patch('builtins.input') as mocked_print:
            app.menu()
            mocked_print.assert_called_with(app.menu_prompt)

    # Test to check if calling menu calls the print_blogs function
    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_with()

    # Test to verify that print_blogs function prints correctly
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('-Test by Test Author(0 post)')

    # Test the functionality of ask_create_blog
    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_post()

            self.assertIsNone(app.blogs.get('Test'))

    # Test to verify ask_read_blog calls print_posts with the correct blog
    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test'])

    # Test to ensure print_posts correctly prints the posts of a blog
    def test_print_posts(self):
        app.blogs['Test'].create_post('Test Post', 'Test Content')

        with patch('app.print_post') as mocked_print_posts:
            app.print_posts(app.blogs['Test'])

            mocked_print_posts.assert_called_with(app.blogs['Test'].posts[0])

    # Test to verify that print_post correctly formats and prints a post
    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
   --- Post title---
   Post content
    '''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    # Test to verify the functionality of ask_create_post
    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')
