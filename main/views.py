import requests
from django.shortcuts import render

def index(request):
    url = "https://api.jikan.moe/v4/seasons/now"

    filtered_anime = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Перевірка на помилки HTTP
        anime_data = response.json()

        if 'data' in anime_data and isinstance(anime_data['data'], list):
            for anime in anime_data['data']:
                title = anime.get('title', 'No title')
                if len(title) > 20:
                    title = title[:20] + '...'

                image_url = (
                    anime.get('images', {}).get('jpg', {}).get('image_url') or
                    anime.get('images', {}).get('jpg', {}).get('small_image_url')
                )

                filtered_anime.append({
                    'title': title,
                    'image': image_url
                })
        else:
            print("Unexpected data format received from API")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Jikan API: {e}")

    return render(request, 'main/index.html', {'anime': filtered_anime})
