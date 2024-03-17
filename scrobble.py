import time
import pylast
import json
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO



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
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=USERNAME, password_hash=PASSWORD)

# Initialize a variable to keep track of the last scrobbled track
last_track = None

# Function to print the scrobbled track to console
def print_new_scrobble(track):
    global last_track
    if last_track is None or last_track != track:
        print(f"New scrobble: {track.title} by {track.artist}")
        last_track = track

# Function to continuously check for new scrobbles
def check_for_scrobbles():
    while True:

        user = network.get_user(USERNAME)
        now_playing = user.get_now_playing()

        if now_playing:

            artist = now_playing.get_artist().name
            album = now_playing.get_album().title
            img = now_playing.get_cover_image()

            add_text_to_image(img, album+"", (200, 50) )
            print(now_playing,'\n',artist,'\n',album,'\n',img,'\n','\n')
            time.sleep(3)
        else:
            print("Nothing Playing")
            time.sleep(1)  # Check every 10 seconds

def load_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def add_text_to_image(image_url, text, position, font_size=20, font_color=(0,0,0), font_path=None):

    # response = requests.get(image_url)
    # image = Image.open(BytesIO(response.content))
    icon = load_image_from_url(image_url)

    # Create a blank image with the desired dimensions
    final_width = 512
    final_height = 200
    background_color = (255, 255, 255)  # White background
    final_image = Image.new("RGB", (final_width, final_height), background_color)

    # Resize and paste the icon on the left side with padding
    padding = 3
    icon_size = (final_height - padding, final_height - padding)
    final_image.paste(icon.resize(icon_size), (padding, padding))

    # Draw text on the right side
    draw = ImageDraw.Draw(final_image)
    font = ImageFont.load_default()  # You can also specify a custom font here
    text = "Hello World"
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((final_width - text_width) // 2, (final_height - text_height) // 2)  # Center the text vertically
    draw.text(text_position, text, fill=(0, 0, 0), font=font)  # Fill with black color

    final_image.save('album.jpeg')

if __name__ == "__main__":
    check_for_scrobbles()
