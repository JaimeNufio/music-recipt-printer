import time
import pylast

# Last.fm credentials
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
USERNAME = "your_username"
PASSWORD = pylast.md5("your_password")

# Authenticate with Last.fm
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=USERNAME, password_hash=PASSWORD)

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
        recent_tracks = user.get_recent_tracks(limit=1)
        if recent_tracks:
            track = recent_tracks[0].track
            print_new_scrobble(track)
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    check_for_scrobbles()
