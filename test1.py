import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_artist_details(artist_name):
    # Set up API credentials
    client_id = '6d18dc785abf4280becf23f23a79012c'
    client_secret = '243b83e815054096875c5cc32b1f0f26'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for the artist
    results = sp.search(q=f'artist:{artist_name}', type='artist')
    if results['artists']['total'] > 0:
        # Get the first artist from the search results
        artist = results['artists']['items'][0]
        
        # Get the artist's followers count
        followers_count = artist['followers']['total']
        
        # Get the artist's popularity score
        popularity = artist['popularity']
        
        # Get the artist's image URL
        image_url = artist['images'][0]['url'] if artist['images'] else None
        
        # Get the artist's genres (first 3)
        genres = artist['genres'][:3] if artist['genres'] else None
        
        # Return the details
        return {
            'followers_count': followers_count,
            'popularity': popularity,
            'image_url': image_url,
            'genres': genres
        }
    else:
        return None

# Example usage
artist_name = 'Achilles'
details = get_artist_details(artist_name)
if details:
    print(f"Details for {artist_name}:")
    print(f"Followers Count: {details['followers_count']}")
    print(f"Popularity: {details['popularity']}")
    print(f"Image URL: {details['image_url']}")
    # print(f"Genres: {', '.join(details['genres'])}")
    print(genres)
else:
    print("Artist not found.")
