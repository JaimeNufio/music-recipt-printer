import time
import pylast
import json
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import math
from recipt import POS_Printer
import datetime

# Last.fm credentials
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
USERNAME = "your_username"
PASSWORD = pylast.md5("your_password")

with open('config.json','r') as file:
    data = json.load(file)['lastfm']

    API_KEY = data['APIKEY']
    API_SECRET = data['SECRET']
    USERNAME = data['USER']
    PASSWORD = pylast.md5(data['PASSWORD'])

# Authenticate with Last.fm
network = pylast.LastFMNetwork(
    api_key=API_KEY, 
    api_secret=API_SECRET, 
    username=USERNAME, 
    password_hash=PASSWORD
    )

last_track = ''
printer = POS_Printer()


def print_new_scrobble(track):
    global last_track
    if last_track is None or last_track != track:
        print(f"New scrobble: {track.title} by {track.artist}")
        last_track = track

# Function to continuously check for new scrobbles
def check_for_scrobbles():
    global last_track
    nothingPlaying = False

    while True:

        user = network.get_user(USERNAME)
        now_playing = user.get_now_playing()

        if now_playing and not last_track == now_playing.title:
            try:
                nothingPlaying = False
                artist = shorten_string(now_playing.get_artist().name)
                album = shorten_string(now_playing.get_album().title,maxSize=60)
                track = shorten_string(now_playing.title)
                img = now_playing.get_cover_image()

                add_text_to_image(img, album, artist, track )
                last_track = now_playing.title
                print("Now Playing: '{}' from '{}' by {}".format(track, album, artist))
                time.sleep(1)
            except Exception as e:
                print(e)
        elif now_playing and last_track == now_playing.title:
            # print(".")
            time.sleep(1)
        else:
            if (not nothingPlaying):
                nothingPlaying = True
                print("Nothing Playing")
            time.sleep(1)  # Check every 10 seconds

def load_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def shorten_string(string, maxSize = 32):
    if len(string) > maxSize:
        # Replace the last 2 characters with ...
        return string[:maxSize-2].strip() + "..."
    else:
        return string

def add_text_to_image(image_url, album, artist, track, font_size=22):

    timestamp = datetime.datetime.now().strftime("%m/%d/%y %I:%M%p")    
    print(timestamp)
    
    icon = load_image_from_url(image_url)

    final_width = 512
    final_height = 128
    background_color = (255, 255, 255)  
    final_image = Image.new("RGB", (final_width, final_height), background_color)

    padding = 10
    icon_size = (final_height - padding*2, final_height - padding*2)
    final_image.paste(icon.resize(icon_size), (padding, padding))

    draw = ImageDraw.Draw(final_image)
    font = ImageFont.truetype("verdana.ttf", font_size)

    track_title = track # + " - " + artist + "\n" + album
    text_position = (final_height,padding)
    draw.text(text_position, track_title, fill=(0, 0, 0), font=font)  

    font = ImageFont.truetype("verdana.ttf", math.floor(font_size*.7))
    track_title = album
    text_position = (final_height,padding+(font_size*1.5))
    draw.text(text_position, track_title, fill=(50, 50, 50), font=font)  

    font = ImageFont.truetype("verdana.ttf", math.floor(font_size*.7))
    track_title = artist
    text_position = (final_height,final_height-(font_size*1.5))
    draw.text(text_position, track_title, fill=(0, 0, 0), font=font)  

    font = ImageFont.truetype("verdana.ttf", math.floor(font_size*.7))
    track_title = timestamp
    text_position = (final_width-150,final_height-(font_size*1.5))
    draw.text(text_position, track_title, fill=(0, 0, 0), font=font)  

    final_image = final_image.convert("L")
    final_image.save('album.jpeg')

    printer.print(path='album.jpeg')

if __name__ == "__main__":
    check_for_scrobbles()
