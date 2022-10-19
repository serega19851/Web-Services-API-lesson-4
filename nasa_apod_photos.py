import requests
from pathlib import Path
import os
from supporting import picture_save, gives_the_file_extension
from dotenv import load_dotenv


def downloading_nasa_photos():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    directory_path = os.path.join(os.path.dirname(__file__), 'images/')
    Path(directory_path).mkdir(parents=True, exist_ok=True)
    params = {'api_key': nasa_api_key, 'count': 30}
    response = requests.get(
        "https://api.nasa.gov/planetary/apod", params=params
    )
    response.raise_for_status()
    for number, url in enumerate(response.json()):
        picture_save(
            url['url'], f'{directory_path}nasa_apod_{number}'
            f'{gives_the_file_extension(url["url"])}'
        )


if __name__ == '__main__':
    downloading_nasa_photos()
