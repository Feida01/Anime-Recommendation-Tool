import json

with open('../data/anime_data.json') as f:
    data = json.load(f)

anime_list = []

for anime in data:
    anime_info = {
        'mal_id': anime['mal_id'],
        'title': anime['title'],
        'type': anime['type'],
        'source': anime['source'],
        'episodes': anime['episodes'],
        'score': anime['score'],
        'genres': [genre['name'] for genre in anime['genres']],
        'themes': [theme['name'] for theme in anime['themes']] if 'themes' in anime else []
    }
    anime_list.append(anime_info)

with open('../data/transformed_anime_data.json', 'w') as outfile:
    json.dump(anime_list, outfile, indent=4)

print("Transformation completed. The transformed data has been written to transformed_anime_data.json.")
