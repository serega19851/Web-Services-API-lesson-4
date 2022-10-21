import requests
import os
from urllib.parse import urlparse, unquote


def save_picture(url, user_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(user_path, 'wb') as file:
        file.write(response.content)


def get_the_file_extension(url):
    link = unquote(url, encoding='utf-8', errors='replace')
    url_component = urlparse(link).path
    return os.path.splitext(url_component)[-1]
