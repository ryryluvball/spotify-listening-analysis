import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ryan_spotify.csv")

artist_count = df['artist'].value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.rcParams['font.family'] = "cursive"
plt.barh(artist_count.index, artist_count.values, color='seagreen')
plt.xlabel('Number of Top Tracks', fontsize=12)
plt.title("Top 10 Artists in Ryan's Spotify Library", fontsize=16, fontweight="bold")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_artists.png")
plt.show()

short = set(df[df['time_range'] == 'short_term']['artist'])
long = set(df[df['time_range'] == 'long_term']['artist'])

recents = short - long
past = long - short

print("Recent obsessions:")
for a in recents:
    print(f" {a}")

print("\nLong-term obsessions:")
for a in past:
    print(f" {a}")
