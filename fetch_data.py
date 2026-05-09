import os
import spotipy
from dotenv import load_dotenv
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='user-top-read user-read-recently-played'))
def get_top_tracks(time_range, limit=50):
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    tracks = []
    for item in results['items']:
        tracks.append({
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name'],
            'release_date': item['album']['release_date'],
            'popularity': item.get('popularity', 0),
            'id': item['id'],
            'time_range': time_range
        })
        
    return(tracks)

all_tracks = []
for tr in ['short_term', 'medium_term', 'long_term']:
    all_tracks.extend(get_top_tracks(tr))

df = pd.DataFrame(all_tracks)

artist_genres = {
    "GIVĒON": "r&b",
    "Lewis Capaldi": "pop",
    "JIHYO": "k-pop",
    "Olivia Rodrigo": "pop",
    "Lil Tecca": "hip hop",
    "HUNTR/X": "k-pop",
    "Travis Scott": "hip hop",
    "DaBaby": "hip hop",
    "Drake": "hip hop",
    "Macklemore": "hip hop",
    "Preme": "hip hop",
    "SZA": "r&b",
    "Future": "hip hop",
    "Swae Lee": "hip hop",
    "Don Toliver": "hip hop",
    "Zedd": "electronic",
    "Yeat": "hip hop",
    "Kelly Clarkson": "pop",
    "KATSEYE": "k-pop",
    "NIKI": "indie pop",
    "24kGoldn": "hip hop",
    "MAGIC!": "reggae fusion",
    "Twenty One Pilots": "alternative",
    "Addison Rae": "pop",
    "Kehlani": "r&b",
    "One Direction": "pop",
    "PARTYNEXTDOOR": "r&b",
    "Brent Faiyaz": "r&b",
    "One Republic": "pop",
    "Calvin Harris": "electronic",
    "Tory Lanez": "hip hop",
    "Robin Schulz": "electronic",
    "USHER": "r&b",
    "Mariah the Scientist": "r&b",
    "Justin Bieber": "pop",
    "James Arthur": "pop",
    "David Guetta": "electronic",
    "Bruno Mars": "pop",
    "Lady Gaga": "pop",
    "The Kid LAROI": "hip hop",
    "Maroon 5": "pop",
    "Melanie Martinez": "alternative pop",
    "Ruth B.": "indie pop",
    "ian": "indie pop",
    "Dominic Fike": "indie pop",
    "Shawn Mendes": "pop",
    "D'Aydrian Harding": "r&b",
    "Carly Rae Jepsen": "pop",
    "Kendrick Lamar": "hip hop",
    "The Weeknd": "r&b",
    "Offset": "hip hop",
    "Ariana Grande": "pop",
    "John Legend": "r&b",
    "Metro Boomin": "hip hop",
    "The Chainsmokers": "electronic",
    "Jason Mraz": "pop",
    "Mr. Probz": "pop",
    "DNCE": "pop",
    "Lauv": "indie pop",
    "Halsey": "alternative pop",
    "Macklemore": "hip hop",
    "DJ Snake": "electronic",
    "Baby Keem": "hip hop",
    "NAV": "hip hop",
    "Niall Horan": "pop",
    "Avicii": "electronic",

}

df['genre'] = df['artist'].map(artist_genres)

df.to_csv("ryan_spotify.csv", index=False)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)