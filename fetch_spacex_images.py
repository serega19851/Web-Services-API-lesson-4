from pathlib import Path
import os
from supporting import save_picture, get_the_file_extension
import requests
import argparse


def gets_spasex_id():
    parser = argparse.ArgumentParser(
        description="The file accepts an optional "
                    "id and uploads photos to a folder"
    )
    parser.add_argument(
        "id", help="Enter the spasex site id ("
        "or run the file without id)", nargs="?"
    )
    args = parser.parse_args()
    return args.id


def get_references():
    last_id = "5eb87d42ffd86e000604b384"
    console_id = gets_spasex_id()
    if console_id is None:
        id = last_id
    else:
        id = console_id
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}")
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def fetch_spacex_last_photographs():
    directory_path = os.path.join(os.path.dirname(__file__), "images/")
    Path(directory_path).mkdir(parents=True, exist_ok=True)
    for number, url in enumerate(get_references()):
        save_picture(
            url, f"{directory_path}spase_x_{number}"
            f"{get_the_file_extension(url)}"
        )


if __name__ == '__main__':
    fetch_spacex_last_photographs()
