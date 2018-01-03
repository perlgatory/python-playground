import plistlib
from collections import Counter


def load_plist(filename):
    with open(filename, 'rb') as fp:
        plist = plistlib.load(fp)
    return plist


def find_duplicates(filename):
    print('Finding duplicate tracks in {}...'.format(filename))
    # read in playlist
    plist = load_plist(filename)
    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # create a track name dictionary
    track_names = Counter()
    # iterate through the tracks
    for trackId, track in tracks.items():
        name = track['Name']
        duration = track['Total Time'] // 1000
        description = (name, duration)
        track_names[description] += 1
    # extract duplicates from track_names
    dups = filter(lambda x: track_names[x] > 1, track_names.keys())
    return list(dups)


def find_common_tracks(filenames):
    # a list of sets of track names
    track_name_sets = []
    for filename in filenames:
        track_names = set()
        plist = load_plist(filename)
    # LEFT OFF HERE


if __name__ == '__main__':
    print(find_duplicates('test-data/mymusic.xml'))