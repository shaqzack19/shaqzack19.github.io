import os
import json
import urllib.parse

def generate_songs_json(folder_path):
    # Initialize an empty list to hold the song data
    songs = []

    # Base URL for accessing raw files on GitHub (change if your structure is different)
    base_url = "https://github.com/shaqzack19/WorkMusic/tree/main/Songs"

    # Walk through the folder and get all mp3 files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.mp3'):
                # Get the song name (remove the .mp3 extension)
                file_name = file.replace('.mp3', '')

                # URL-encode the song name to handle special characters
                encoded_file_name = urllib.parse.quote(file_name)

                # Construct the full URL to the raw file
                file_url = f"{base_url}{encoded_file_name}.mp3"

                # Create a dictionary for the song
                song = {
                    'name': file_name,
                    'path': file_url
                }

                # Add the song to the list
                songs.append(song)

    # Write the list to a JSON file
    with open('songs.json', 'w') as json_file:
        json.dump(songs, json_file, indent=4)

    print(f'Successfully generated songs.json with {len(songs)} songs.')

if __name__ == '__main__':
    # Specify the path to your Songs folder (change 'Songs' to the name of your folder)
    folder_path = 'Songs'
    generate_songs_json(folder_path)
