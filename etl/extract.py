import requests
import json
import time


def retrieve_top_anime(pages):
    new_anime_data = []
    url = "https://api.jikan.moe/v4/top/anime"

    for page in range(1, pages + 1):
        params = {"page": page}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            anime_data_page = data.get("data", [])
            new_anime_data.extend(anime_data_page)

            print(f"Retrieved page {page} of top anime.")
        else:
            error_message = response.json().get("message", "Unknown error occurred")
            print(f"An error occurred while retrieving page {page} of top anime: {error_message}")

        time.sleep(1)

    return new_anime_data


num_pages = 20

anime_data = retrieve_top_anime(num_pages)

with open("data/anime_data.json", "w") as json_file:
    json.dump(anime_data, json_file)

num_anime_extracted = len(anime_data)

print(f"Total anime extracted: {num_anime_extracted}")
print("All anime data saved as anime_data.json.")
