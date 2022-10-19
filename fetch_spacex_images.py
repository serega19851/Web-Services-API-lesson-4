from pathlib import Path
import os
from supporting import picture_save, gives_the_file_extension
import requests
import argparse


def gets_spasex_id():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="display id", nargs='?')
    args = parser.parse_args()
    return args.id


def returns_references():
    if gets_spasex_id() is None:
        response = requests.get(
            f'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
        )
        response.raise_for_status()
        return response.json()['links']['flickr']['original']
    response = requests.get(
        f'https://api.spacexdata.com/v5/launches/{gets_spasex_id()}'
    )
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_last_launch():
    directory_path = os.path.join(os.path.dirname(__file__), 'images/')
    Path(directory_path).mkdir(parents=True, exist_ok=True)
    for number, url in enumerate(returns_references()):
        picture_save(
            url, f'{directory_path}spase_x_{number}'
            f'{gives_the_file_extension(url)}'
        )


if __name__ == '__main__':
    fetch_spacex_last_launch()
