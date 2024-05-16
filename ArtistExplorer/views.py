from django.shortcuts import render ,redirect,get_object_or_404
from ArtistExplorer.models import Artists
from django.http import JsonResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



def index(request):
    artists = Artists.objects.all()
    return render(request , 'index.html' , {'Artist' : artists})



from django.http import JsonResponse
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
# Import Artists model assuming it's defined elsewhere in your project
from.models import Artists

def add(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        
        client_id = '6d18dc785abf4280becf23f23a79012c'
        client_secret = '243b83e815054096875c5cc32b1f0f26'
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Search for the artist
        results = sp.search(q=f'artist:{name}', type='artist')
        if results['artists']['total'] > 0:
            # Get the first artist from the search results
            artist = results['artists']['items'][0]
            
            followers = artist['followers']['total']    
            followers_count = "{:,.2f}M".format(followers / 1000000)
            popularity = artist['popularity']
            image_url = artist['images'][0]['url'] if artist['images'] else None
            genres = artist['genres'][:3] if artist['genres'] else None
            
            # Initialize Description and Popularity variables
            description = ""
            popularity_value = popularity
            
            # Append genres to Description
            try:
                for genre in genres:
                    description += genre + ", "
            except TypeError:
                print("Error: genres is not iterable.")
            
            # Create and save the artist instance
            Artist = Artists(
                Name=name,
                Description=description.rstrip(", "),  # Remove trailing comma and space
                Popularity=popularity_value,
                Image=image_url,
                Followers=followers_count
            )
            Artist.save()
            
            return redirect('home')  # Redirect to the home page after saving
        else:
            return JsonResponse({'error': 'Artist not found'}, status=404)
    else:
        return render(request, 'index.html')  # Render the form if the request method is not POST


def edit(request):
    Artist = Artists.objects.all()
    
    context = {
        'Artist' : Artist
    }
    
    return redirect(request , 'index.html' , context)


def update(request, pk):
    
    artist = get_object_or_404(Artists, pk=pk)
    
    
    if request.method == 'POST':
        artist.Name = request.POST.get('Name')
        artist.Description = request.POST.get('Description')
        artist.Popularity = request.POST.get('Popularity')
        artist.Followers = request.POST.get('Followers')
        # artist.Image = request.FILES.get('Image')
        
        
        artist.save()
        
        # Redirect to a success page or back to the list of artists
        return redirect('home')  




def delete(request, pk):
    artist = get_object_or_404(Artists, pk=pk)
    artist.delete()
    return redirect('home')  