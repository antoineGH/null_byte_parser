import secrets
import os
import requests

def save_image(image, directory, picture_fn):
    directory_path = os.path.join(os.getcwd(), 'static', directory)
    picture_path = os.path.join(directory_path, picture_fn)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    with open(picture_path, 'wb') as img:
        img.write(requests.get(image).content)
        print(f"Image saved in {picture_path}")

def name_image(image):
    random_hex = secrets.token_hex(8)
    tupple_file_ext = os.path.splitext(image)
    picture_ext = tupple_file_ext[1]
    picture_fn = random_hex + picture_ext

    return picture_fn
