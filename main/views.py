import requests
from django.shortcuts import render

def index(request):
    top_anime_url = "https://api.jikan.moe/v4/top/anime"
    new_anime_url = "https://api.jikan.moe/v4/seasons/now"

    top_anime = []
    new_anime = []

    try:
        # Отримуємо топ аніме
        top_response = requests.get(top_anime_url)
        top_response.raise_for_status()
        top_anime_data = top_response.json()

        if 'data' in top_anime_data and isinstance(top_anime_data['data'], list):
            for anime in top_anime_data['data'][:5]:  # Беремо лише топ 5
                title = anime.get('title', 'No title')
                if len(title) > 20:
                    title = title[:20] + '...'

                image_url = (
                    anime.get('images', {}).get('jpg', {}).get('image_url') or
                    anime.get('images', {}).get('jpg', {}).get('small_image_url')
                )

                top_anime.append({
                    'title': title,
                    'image': image_url
                })
        else:
            print("Unexpected data format received from top anime API")

        # Отримуємо нові аніме
        new_response = requests.get(new_anime_url)
        new_response.raise_for_status()
        new_anime_data = new_response.json()

        if 'data' in new_anime_data and isinstance(new_anime_data['data'], list):
            for anime in new_anime_data['data']:
                title = anime.get('title', 'No title')
                if len(title) > 20:
                    title = title[:20] + '...'

                image_url = (
                    anime.get('images', {}).get('jpg', {}).get('image_url') or
                    anime.get('images', {}).get('jpg', {}).get('small_image_url')
                )

                new_anime.append({
                    'title': title,
                    'image': image_url
                })
        else:
            print("Unexpected data format received from new anime API")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Jikan API: {e}")

    return render(request, 'main/index.html', {'top_anime': top_anime, 'new_anime': new_anime})
