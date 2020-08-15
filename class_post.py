import json
from datetime import datetime
import os
from models import Blog, session
from utils import save_image

# Posts class to handle singular post
class Posts:
    nb_post = session.query(Blog).count()

    def __init__(self):
        self.posts = []

    # Adding post to Posts.posts if not in DB
    def add_post(self, post):
        if self.already_exist(post.link):
            print(f"Post {post.title} already exists.")
        else:
            # Adding post to Posts.posts
            self.posts.append(post)
            Posts.nb_post += 1

            # Saving image
            try:
                save_image(post.image, 'null_byte', post.picture_fn)
            except Exception as e:
                print("Couln\'t save file")

            # Adding post to Database
            try:
                post = Blog(link=post.link, title=post.title, summary=post.summary, image=post.image, picture_fn=post.picture_fn, article_content=post.article_content)
                session.add(post)
                session.commit()
                print(f"Adding {post.title} to the database.")
            except Exception as e:
                print(f"Couln\'t add {post.title} to the database.")


    # Removing post from Posts.posts using link
    def remove_post(self, link):
        for post in self.posts:
            if post.link == link:
                self.posts.remove(post)
                Posts.nb_post -= 1
                print(f"Removing {post.title} from Posts.")
                break

    # Export Posts.posts to JSON file
    def save_json(self, filename):
        date = datetime.now().strftime("%d-%m-%y_%H-%M-%S_")
        directory_path = os.path.join(os.getcwd(), 'static', date + filename)
        serialized = []

        for post in self.posts:
            serialized.append(post.serialize)

        try:
            with open(directory_path, 'w') as json_file:
                json.dump(serialized, json_file)
                print(f"Saving Json file in {directory_path}")
        except Exception:
            print(f"Can't save Json file in {directory_path}")

    # Check from DB is link is already existing
    def already_exist(self, link):
        post = session.query(Blog).filter(Blog.link == link).first()
        if post:
            return True
        return False

class Post:
    def __init__(self, link, title, summary, image, picture_fn, article_content):
        self.link = link
        self.title = title
        self.summary = summary
        self.image = image
        self.picture_fn = picture_fn
        self.article_content = article_content

    def __repr__(self):
        return f"Post Object - {self.title}"

    # Serialize from object to dictionnary
    @property
    def serialize(self):
        return {
            'link': self.link,
            'title': self.title,
            'summary': self.summary,
            'image': self.image,
            'picture_fn': self.picture_fn,
            'article_content': self.article_content
        }

# # Testing 
# posts = Posts()

# print(posts.nb_post)
# print(posts.posts)

# post1 = Post('lol', 'lol', 'lol', 'lol', 'lol', 'lol')
# post2 = Post('lil', 'lil', 'lil', 'lil', 'lil', 'lil')
# post3 = Post('lol', 'lol', 'lol', 'lol', 'lol', 'lol')

# posts.add_post(post1)
# posts.add_post(post2)
# posts.add_post(post3)


# print(posts.nb_post)
# print(posts.posts)
