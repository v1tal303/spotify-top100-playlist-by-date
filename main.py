import requests
from bs4 import BeautifulSoup
import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials below

SPOTIFY_ID = config.spotify_id
SPOTIFY_SECRET = config.spotify_secret

# Query the user for a date in YYYY-MM-DD format. Then with BeautifulSoup scrape relevant information required for
# spotify API.

user_date = input("Which year do you want to travel to? Please type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}/")
song_web_page = response.text
soup = BeautifulSoup(song_web_page, "html.parser")
list_of_artists_html = soup.find_all(name="h3", id="title-of-a-story", class_=["u-line-height-125"])
list_of_songs_html = soup.find_all(name="span", class_="a-no-trucate")
list_of_artists = [i.getText().strip("\n") for i in list_of_artists_html]
list_of_songs = [i.getText().strip("\n") for i in list_of_songs_html]
song_dict = dict(zip(list_of_artists, list_of_songs))

# Spotify API set-up

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spotify.current_user()["id"]

# Use the song_dict dictionary to find songs on Spotify and build the playlist.

tracks = []
track_list = []
song_uri = []

for k, v in song_dict.items():
    result = spotify.search(q=k + " " + v, type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"The song {k}:{v} does not exist")

playlist = spotify.user_playlist_create(user=user_id, name=f"{user_date} Top 100 Songs!", public=False)
added_tracks = spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uri)


