import requests
from pathlib import Path
import os
from supporting import save_picture
import datetime
from dotenv import load_dotenv


def downloading_epic_photos():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    directory_path = os.path.join(os.path.dirname(__file__), 'images/')
    Path(directory_path).mkdir(parents=True, exist_ok=True)
    params = {'api_key': nasa_api_key}
    response_day = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params=params
    )
    response_day.raise_for_status()
    date = datetime.datetime.fromisoformat(response_day.json()[-1]['date'])
    formatted_date = date.strftime("%Y/%m/%d")
    response = requests.get(
        f"https://api.nasa.gov/EPIC/api/natural/date/{date}",
        params=params)
    response.raise_for_status()
    for number, filename in enumerate(response.json()):
        response = requests.get(
            f'https://api.nasa.gov/EPIC/archive/natural/'
            f'{formatted_date}/png/{filename["image"]}.png', params=params
        )
        response.raise_for_status()
        save_picture(response.url, f'{directory_path}nasa_epic_{number}.png')


if __name__ == '__main__':
    downloading_epic_photos()
