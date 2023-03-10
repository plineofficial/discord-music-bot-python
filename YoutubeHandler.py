from youtube_dl import YoutubeDL
from requests import get

def search(query):
    with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
        try: get(query)
        except: info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
        else: info = ydl.extract_info(query, download=False)
    return (info, info['formats'][0]['url'])
