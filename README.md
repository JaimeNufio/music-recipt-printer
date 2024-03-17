## Live Music Scrobble Printer

### Elevator Pitch ( aka, the '*TL;DR*' )

I thought it'd be neat if I could take the music I'm scrobbling through lastFM, and fed it through a recipt printer. 

### More Poetic Explanation

Spotify Wrapped is always a big time of the year for music lovers; there is clearly a communal spirit to sharing music tastes efficently. Continuing with this thought, the digital age has introduced us to streaming, an ephemeral form of consumption that kinda dominates how we interact with our media. Shows, movies, videos, and music are consumed and forgotten barring the truly exceptional or in agregate from events like Spotify Wrapped. I made this in hopes of letting this run passively in my home, collecting data the same way LastFM does, whilst having a physical representation of exactly how much and what music I listen to.

### Sample Image:
![Sample Entry](album_example.jpeg)

### Requirements:

- [A LastFM account linked to some service for Scrobbling.](https://www.last.fm/about/trackmymusic)
- A TM-T88V or similar Thermal Printer
- The Correct Drivers
- Patience to troubleshoot Windows

### Setup:
 
0) Clone this repo, `cd` into it. run `pip  install -r requirements.txt`

1) Before you can run the program, you must get the printers Windows drivers correctly installed (you may need Zadig to install drivers) and must have also installed the EPSON printer's drivers on your machine. [This guide was really helpful.](https://nyorikakar.medium.com/printing-with-python-and-epson-pos-printer-fbd17e127b6c)

    - [EPSON Drivers can be found here](https://epson.com/Support/Point-of-Sale/OmniLink-Printers/Epson-TM-T88VI-Series/s/SPT_C31CE94061?review-filter=Windows+10+64-bit).

2) Edit the *config.json* to reflect your LastFM application and login, as well as your printers VendorID and ProductID. You can find those values in device manager on Windows.

3) Run `python scrobble.py`, and play some music on... whatever service you've linked your lastFM account to scrobble from. Typically Spotify or Youtube.
