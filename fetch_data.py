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

df.to_csv("ryan_spotify.csv", index=False)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)