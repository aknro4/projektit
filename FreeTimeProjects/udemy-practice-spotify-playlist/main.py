from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# Just in case
SPOTIFY_TOKEN = "http://example.com/?code=AQCfSIcvsbUxXZJPij_zmzM1uZjaPvmE37nKk4VMew42bHFrEwab3CjYcnuK_E4OJZSRITAJd6sh-H01TnnswKkGgGeV-lR5JPUdWHT8hPUPHK8aUjtAUEpaNVhaGZbY4Bl4c16GmBVspsrHkVaVZ8y0_wAiwVlZvnwzp1PmtTjIiQg4jh5ZU-4"

SPOTIPY_CLINET_ID = "4c9114e1a1be4f0a89ee60f286b79549"
SPOTIPY_CLIENT_SECERET = "4a87eaf2700644b2ad02e2f1c1ac9dfc"
SPOTIPY_REDIRECT_URI = "http://example.com"
USER = "Chroma"

user_date = input("Which year do you want to travel to? Type date formatted YYYY-MM-DD: ")


response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_date}")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
songs = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
all_artist = soup.find_all(name="span", class_="a-no-trucate")
song_names = [song.getText().split() for song in songs]
# For in depth research. Doesn't work sadly. Or im the one to blame
artists = [artis.getText().split()[0:1] for artis in all_artist]


joined_songs = []
for i in range(0, len(song_names)):
    x = " ".join(song_names[i])
    joined_songs.append(x)


print(joined_songs)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLINET_ID,
                                               client_secret=SPOTIPY_CLIENT_SECERET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               cache_path=".cache",
                                               show_dialog=True,
                                               ))

user_id = sp.current_user()["id"]
year = user_date.split("-")[0]
song_uris = []
for song in joined_songs:
    # for artist in artists: , artist={artis}
    result = sp.search(q=f"track={song},year={year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Song: {song} was not found")

# maybe should check if there is already playlist created with that date
playlist = sp.user_playlist_create(user=user_id, name=f"Top 100 songs from {user_date}", public="false")
# search that created playlist whit id and add items
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

playlist_details = sp.playlist(playlist_id=playlist["id"])

print("Spotify playlist link: ", playlist_details["external_urls"]["spotify"])

