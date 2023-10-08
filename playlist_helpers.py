# NOTE: DO NOT EDIT `display_playlist` and `add_song`


def display_playlist(playlist):
    # This function prints out what is in your playlist
    # Takes one argument: 'playlist' (a list)
    if len(playlist) == 0:
        print('Playlist is empty!')
    else:
        for i in range(len(playlist)):
            print(
                f'Track {i + 1}: {playlist[i]["plays"]} plays\n\t- {playlist[i]["title"]} by {playlist[i]["artist"]}'
            )


def add_song(playlist, song):
    # This function ads a song to the playlist
    # Takes two arguments: 'playlist' (a list), and 'song' (a dictionary)
    # Automatically initialize play count of song to 0
    song['plays'] = 0
    playlist.append(song)

'''
6.1 TODO: Define a function called `get_playlist_length`
This function should have one parameter called 'playlist'
The function should return an integer value indicating how many songs there are
The function should NOT print anything out
'''
def get_playlist_length(playlist):
    lenth = int(len(playlist))
    return lenth

'''
9.0 TODO: Define a function `called play_track`
It should have two parameters
-'playlist' (a list)
-'track' (an integer) - this should be optional, and by default play track 1
This function should 'play' the song corresponding to the input track #
For example play_track(my_playlist, 3) should print out:
'Now playing Track 3: Controversy by Prince' 
Assuming that Controverthe third track in your playlist 'sy' by 'Prince'
This function should ALSO increase the 'plays' value for that song's dictionary by 1
So, if 'Controversy' has 0 plays so far, it should now be increased to 1
'''

def play_track(playlist, track = None ):
    if track == None:
        song_ind = 0
        song_name = playlist[song_ind]["title"]
        song_art = playlist[song_ind]["artist"]
        playlist[song_ind]['plays'] += 1
        print(f'Now playing Track {track}: {song_name} by {song_art}')
    elif track < 1 or track > len(playlist):
        return track
    # elif len(playlist): 
    else:
        song_ind = track - 1
        song_name = playlist[song_ind]["title"]
        song_art = playlist[song_ind]["artist"]
        playlist[song_ind]['plays'] += 1
        print(f'Now playing Track {track}: {song_name} by {song_art}')
    

        # print(f'Now playing Track {track}: {playlist[track -1]["title"]} by {playlist[track -1]["artist"]}')
        # playlist[track -1]["plays"] += 1

    # len(playlist) + 1 < track:
    #     print(f'Now playing Track 1: {playlist[0]["title"]} by {playlist[0]["artist"]}')
    # elif len(playlist) + 1 >= track:
    #     print(f'Now playing Track ({track} + 1): {playlist[track]["title"]} by {playlist[track]["artist"]}')
    #     playlist[track]['plays'] += 1
        
    
