import requests
import json
import time
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer


def load_transformed_data(file_path):
    with open(file_path) as f:
        transformed_data = json.load(f)
    return transformed_data


file_path = '../data/transformed_anime_data.json'

transformed_data = load_transformed_data(file_path)

all_genres = set()
all_themes = set()

for anime in transformed_data:
    genres = anime['genres']
    themes = anime['themes'] if 'themes' in anime else []

    all_genres.update(genres)
    all_themes.update(themes)

anime_genres = list(all_genres)
anime_themes = list(all_themes)

seen_anime_titles = ['Horimiya: Piece', 'Horimiya', 'Kimi wa Houkago Insomnia', 'Kaguya-sama wa Kokurasetai: Ultra Romantic']

seen_animes = [anime['mal_id'] for anime in transformed_data if anime['title'] in seen_anime_titles]

user_preferences = {
    'genres': ['Romance'],
    'themes': ['School']
}

print(f'You already watched: {seen_anime_titles}')
print(f'You like: {user_preferences}')

similarities = {}

mlb = MultiLabelBinarizer(classes=anime_genres + anime_themes)
user_preferences_encoded = mlb.fit_transform([user_preferences['genres'] + user_preferences['themes']])

item_profiles = {}

for anime in transformed_data:
    item_id = anime['mal_id']
    item_profile = {
        'title': anime['title'],
        'genres': anime['genres'],
        'themes': anime['themes'] if 'themes' in anime else []
    }
    item_profiles[item_id] = item_profile

filtered_item_profiles = {item_id: item_profile for item_id, item_profile in item_profiles.items() if item_id not in seen_animes}

for item_id, item_profile in filtered_item_profiles.items():
    item_profile_vector = item_profile['genres'] + item_profile['themes']

    item_profile_encoded = mlb.transform([item_profile_vector])

    similarity_score = cosine_similarity(user_preferences_encoded, item_profile_encoded)[0][0]
    similarities[item_id] = similarity_score

sorted_items = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
top_recommendations = [item_id for item_id, similarity_score in sorted_items if item_id not in seen_animes][:5]

base_url = 'https://api.jikan.moe/v4/anime/'

for item_id in top_recommendations:
    anime_url = f'{base_url}{item_id}'
    response = requests.get(anime_url)
    anime_data = response.json()

    title = anime_data['data']['title']

    print(f'I recommend: {title}')

    time.sleep(1)
