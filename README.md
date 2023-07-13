# Anime-Recommendation-Tool

This Anime Recommendation Tool is a Python program that uses data transformation and cosine similarity to provide personalized anime recommendations based on user preferences.

### Requirements

To run the Anime Recommendation Tool, you need to have the following requirements installed:

- Python 3.9 or higher
- requests module
- json module
- time module
- scikit-learn library

## Content-Based Filtering

- The extract.py script makes requests to the Jikan API, It extracts the top anime page to get data of 25 anime per request. The extracted data is then saved as a JSON file.

- The transform.py script reads the extracted data JSON file and transforms it into a more suitable format for the algorithm.

- The recommendation.py script uses the transformed data to generate recommendations based on the user's preferences. It calculates the similarity between the user's preferences and the hardcoded anime preference using cosine similarity.

- The program generates a list of recommendations based on the highest similarity scores, excluding the watched anime.
