from spotipy import *
import time
from uguitar.ug_simplesearch import search
import urllib.parse
import re
import webbrowser

songCache = ""

def updateCache(titleAndArtist):
    global songCache
    if (songCache == titleAndArtist):
        return False
    else:
        songCache = titleAndArtist
        return True

def getCurrentlyPlayingTitleAndArtist(currentTrack):
    currentTrackName = currentTrack["item"]["name"]
    pattern = re.compile(r'\(.*\)')
    currentTrackName = pattern.sub(" ", currentTrackName)
    currentTrackName = removeSpecialCharacters(currentTrackName)
    currentTrackArtist = currentTrack["item"]["artists"][0]["name"]
    currentTrackArtist = removeSpecialCharacters(currentTrackArtist)
    return currentTrackName + " " + currentTrackArtist

def removeSpecialCharacters(trackString):
    return trackString.replace("?", "")

def getSpotifyClient(CLIENT_ID, CLIENT_SECRET):
    token = util.prompt_for_user_token("achinvitha",
                               scope='user-read-playback-state',
                               client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               redirect_uri="http://0.0.0.0/")
    return Spotify(auth=token)

def getClientInformation():
    clientInformationFilePath = "./secret.txt"
    clientIDLocation = 1
    clientSecretLocation = 3
    clientInformationFile = open(clientInformationFilePath, "r")
    clientInformation = clientInformationFile.readline().split(",")
    return clientInformation[clientIDLocation], clientInformation[clientSecretLocation]

if __name__ == "__main__":
    CLIENT_ID, CLIENT_SECRET = getClientInformation()
    spotifyClient = getSpotifyClient(CLIENT_ID, CLIENT_SECRET)
    while True:
        time.sleep(1)
        currentTrack = spotifyClient.current_user_playing_track()
        try:
            currentTitleAndArtist = getCurrentlyPlayingTitleAndArtist(currentTrack)
            if (updateCache(currentTitleAndArtist)):
                url = search(urllib.parse.quote(currentTitleAndArtist))
                webbrowser.open(url, new=0, autoraise=True)
        except Exception as e:
            print(e)