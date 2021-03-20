"""
Functions to play a song / send an email to alert of ticket change
"""
import subprocess

SONG_LINK = "/Users/chris/Music/Music/Media/Music/BBC News/Unknown Album/BBC News Countdown Theme 2014 (Extended Club Remix).mp3"

def playSong():
    subprocess.run(['open', SONG_LINK])

def startTicketAlerts():
    playSong()


