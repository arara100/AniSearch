from django.shortcuts import render
import requests


def anime(request):
    statuses = request.GET.getlist('status')
    types = request.GET.getlist('type')
    order_by = request.GET.get('order_by', 'score')
    genres = request.GET.getlist('genre')
    themes = request.GET.getlist('theme')

    url = f"https://api.jikan.moe/v4/anime?order_by={order_by}"

    if statuses:
        url += "&status=" + ",".join(statuses)

    if types:
        url += "&type=" + ",".join(types)

    if genres:
        url += "&genres=" + ",".join(genres)

    if themes:
        url += "&themes=" + ",".join(themes)

    response = requests.get(url)
    anime_data = response.json()

    filtered_anime = []
    for anime in anime_data['data']:
        title = anime['title']
        if len(title) > 20:
            title = title[:20] + '...'

        image_url = anime['images']['jpg'].get('image_url') or anime['images']['jpg'].get('small_image_url')

        filtered_anime.append({
            'title': title,
            'image': image_url
        })

    return render(request, 'catalog/catalog.html', {'anime': filtered_anime})
