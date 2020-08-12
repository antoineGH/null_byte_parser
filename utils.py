import secrets
import os
import json
import requests

posts = []

def save_image(image, directory):
    random_hex = secrets.token_hex(8)
    tupple_file_ext = os.path.splitext(image)
    picture_ext = tupple_file_ext[1]
    picture_fn = random_hex + picture_ext
    directory_path = os.path.join(os.getcwd(), 'static', directory)
    picture_path = os.path.join(directory_path, picture_fn)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    with open(picture_path, 'wb') as img:
        img.write(requests.get(image).content)

    return picture_fn

def post_posts(title, summary, link, image, picture_fn):
    post = {"title": title, "summary": summary, "link": link, "image": image, "picture_fn": picture_fn}
    posts.append(post)
    return posts

def save_json(json_object):
    try:
        with open('posts.json', "w") as json_file:
            json.dump(json_object, json_file)
            return 'Json Saved as posts.json'
    except Exception:
        pass
