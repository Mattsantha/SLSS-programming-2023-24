# Spotify Analyzer
# Author: Matt
# 16 January 2024

import csv 

# Create a funtion tthat earches through dtata
# Finds all songs from a given artist

def find_all_songs(artist: str) -> list: 
    """Searches through a set of data and returns all songs found from a given
    
    Returns:
        list of sound songs, an empty list if none are found
        """

    # Open the file
    with open("./spotify.csv") as f:
        # ---- Search for all Drake songs
        # ---- USe linear search 
        # create a csv reader object
        csv_reader = csv.DictReader(f)

        # Make a list to stroe all Drake songs
        songs = []

        # Create a coiunyer to stroe the current line numeebr 
        line_num = 0

        # For every line in the file 
        for line in csv_reader: 
            #if its a firts line, print out all the headings
            if line_num == 0:
                #print("The columns are: ")

                # Prints on one line
                #print(",".join(line))

                # Print one on every line
                # for item in line:
                #   print(item)

                line_num += 1
            else:
                # If the artist for thissomng is the given artist
                # Store the song in the list
                    # ---- artist,song tittle, danceability
                if artist.lower() in line['artist'].lower():
                    songs.append((
                        line['artist'],
                        line['song_title'],
                        line['valence'],
                        line['danceability']
                    ))
                line_num += 1

        return songs

drake_songs = find_all_songs("drake")
ed_sheran_songs = find_all_songs("ed shearan")
kendrick_songs = find_all_songs("kendrick")

#print out drake songs that have a danceability of 0.5 or higher
#for song in kendrick_songs:
    #if float(song[-1]) >= 0.5:
       # print(song)


# Right now our songs have three pieces of info:
#    - artist
#    - song title
#    - danceability
# Can you add one more piece of info for every song:
#    - valence
# Right now: ('artist', 'song_title', 'danceability')
# Change: ('artist', 'song_title', 'valence', 'danceability')

# --- Sort using SLECTION sort from smallest to biggest
#   - Dancebility

# Startibg at the begging of the list until the end
for i, song in enumerate(drake_songs):
    # Set the current item to the smnallest danceability
    smallest_dancebility = song[-1]
    smallest_idx = i

    # For the rest of the list
    for j in range(i + 1, len(drake_songs)):
        # If the current item is smaller than smallest
        if drake_songs[j][-1] > smallest_dancebility:
            # Set the smallest danceability with the current
            smallest_dancebility = drake_songs[j][-1]
            smallest_idx = j
        
    # Swap the smalllest danceability with the current item
    drake_songs[i], drake_songs[smallest_idx] = (
        drake_songs[smallest_idx],
        drake_songs[i]
    )

for song in drake_songs:
     print(song)

# can you modify the code so that it sorts from biggest to smallest
