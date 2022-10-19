import requests
import os
from urllib.parse import urlparse, unquote


def picture_save(url, user_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(user_path, 'wb') as file:
        file.write(response.content)


def gives_the_file_extension(url):
    link = unquote(url, encoding='utf-8', errors='replace')
    url_component = urlparse(link).path
    return os.path.splitext(url_component)[-1]
