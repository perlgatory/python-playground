import plistlib
from collections import Counter

def findDuplicates(fileName):
    print('Finding duplicate tracks in {}...'.format(fileName))
    # read in playlist
    with open(fileName, 'rb') as fp:
        plist = plistlib.load(fp)
    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # create a track name dictionary
    trackNames = Counter()
    # iterate through the tracks
    for trackId, track in tracks.items():
        name = track['Name']
        duration = track['Total Time'] // 1000
        description = (name, duration)
        trackNames[description] += 1

