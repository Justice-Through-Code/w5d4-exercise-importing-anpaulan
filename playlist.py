# Music playlist challenge!
# In this challenge, you'll have to both work on this script, and the accompanying script playlist_helpers.py
# All of your functions should be in the other script (playlist_helpers.py)
# But, you'll run your functions here
# NOTE: Since there is no user input in this assignment, feel free to leave your function calls uncommented when you turn it in!

# 1.0 TODO: Import all of the functions in playlist_helpers.py into this file
from playlist_helpers import *
import numpy as np
# import numpy as np
# This code initializes your playlist as an empty list. No songs in it yet!
my_playlist = []


# 2.0 TODO: Check what is in your playlist using the display_playlist() function
# NOTE: Look at the display_playlist() function in playlist_helpers.py to figure out how to use it
display_playlist(my_playlist)

# 3.0 TODO: Add a song to my_playlist using the add_song() function
# The song that you add should be a dictionary, with the following key-value pairs
# 'artist' (string)
# 'title' (string)
# NOTE: Your songs can be whatever you want! The tests will check your FUNCTIONS with their own
# input, not your print statements (:
add_song(my_playlist, {"artist": "ja rule" , "title" : "new york"})
# print(type(my_playlist))
'''
example_song = {'artist': 'Lauryn Hill', 'title': 'Everything Is Everything'}
'''


# 4.0 TODO: Check that you've added the song by running the display_playlist() function again
display_playlist(my_playlist)

# 5.1 TODO: Add 2 more songs to my_playlist (using the add_song function)

add_song(my_playlist, {"artist": "jay z" , "title": "empire state of mind"})
add_song(my_playlist, {"artist": "nas" , "title" : "n.y. state of mind"})

# 5.2 TODO: Then display it again using the display_playlist() function
display_playlist(my_playlist)

# 6.1 TODO: In playlist_helpers.py, define a function called get_playlist_length()
# See playlist_helpers.py for details on how to define this function
# def get_playlist_length(playlist):
#     lenth = int(len(my_playlist))
#     return lenth

# 6.2 TODO: Call the get_playlist_length function you just created in THIS script
# to get the length of my_playlist (make sure you print out the result here!)
print(get_playlist_length(my_playlist))

# 7.0 TODO: At the top of this script, import numpy using the usual alias


# Using numpy, calculate the average monthly plays for a song--
# 8.0 TODO: using the mean() function from numpy, calculate and print the average of monthly_plays
# You don't have to write any functions for this question
monthly_plays = [127030, 274920, 232453, 98278, 500301, 235462]
# (np.mean(monthly_plays))

# 9.0 TODO: In playlist_helpers.py, define a new function called play_track()
# See playlist_helpers.py for details on how to define this function
# In this file, play a few tracks, and run display_playlist() again to make sure it works
play_track(my_playlist, 3)
play_track(my_playlist, 2)
play_track(my_playlist, )
# display_playlist(my_playlist)