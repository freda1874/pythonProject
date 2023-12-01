import blog

menu_prompt = "Enter 'C' to create a blog,'I' to list blogs,'r' to read one,'p' to create a post,or 'q' to quit:"
blogs = dict()  # blog_name:Blog_oject
post_template = '''
   --- {}---
   {}
    '''


def menu():
    print_blogs()
    selection = input(menu_prompt)
    while selection.lower() != 'q':
        if selection.lower() == 'c':
            ask_create_blog()
        elif selection.lower() == 'i':
            print_blogs()
        elif selection.lower() == 'r':
            ask_read_blog()
        elif selection.lower() == 'p':
            ask_create_post()
        selection = input(menu_prompt)


def print_blogs():
    for key, element in blogs.items():
        print("-{}".format(element))


def ask_create_blog():
    # def __init__(self, title, author):
    title = input('Enter blog title: ')
    author = input('Enter blog author name: ')
    blogs[title] = blog.Blog(title, author)


def ask_read_blog():
    title = input('Enter the blog tile you want to read: ')

    print_posts(blogs[title])


def print_posts(title):
    for post in title.posts:
        print_post(post)


def print_post(post):
    print(post_template.format(post.title, post.content))


def ask_create_post():
    # create a post
    blog_name = input('Enter the blog title you want to write a post in: ')
    post_title = input('Enter your post title: ')
    content = input('Enter your post content: ')

    blogs[blog_name].create_post(post_title, content)
