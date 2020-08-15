import json
import os

class Posts:
    nb_post = 0

    def __init__(self):
        # Init from existing post in DB
        self.posts = []

    def add_post(self, post):
        if self.already_exist(post.link):
            print("Post already exists.")
        else:
            self.posts.append(post)
            Posts.nb_post += 1
            print(f"Adding {post.title} to Posts.")

    def remove_post(self, link):
        for post in self.posts:
            if post.link == link:
                self.posts.remove(post)
                Posts.nb_post -= 1
                print(f"Removing {post.title} from Posts.")
                break

    def save_json(self, filename):
        directory_path = os.path.join(os.getcwd(), 'static', filename)
        serialized = []

        for post in self.posts:
            serialized.append(post.serialize)

        try:
            with open(directory_path, 'w') as json_file:
                json.dump(serialized, json_file)
                print(f"Saving Json file in {directory_path}")
        except Exception:
            print(f"Can't save Json file in {directory_path}")

    def already_exist(self, link):
        # Update to check directly DB with SQLAlchemy
        for post in self.posts:
            if post.link == link:
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

