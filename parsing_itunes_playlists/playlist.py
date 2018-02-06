import plistlib
from collections import Counter
import numpy as np
from matplotlib import pyplot


def load_plist(filename):
    with open(filename, 'rb') as fp:
        plist = plistlib.load(fp)
    return plist

def get_track_description(track):
    name = track['Name']
    duration = track['Total Time'] // 1000
    return (name, duration)

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
        description = get_track_description(track)
        track_names[description] += 1
    # extract duplicates from track_names
    dups = filter(lambda x: track_names[x] > 1, track_names.keys())
    return list(dups)


def find_common_tracks(filenames):
    print('Finding common tracks in {}...'.format(filenames))
    # a list of sets of track names
    track_name_sets = []
    for filename in filenames:
        track_names = set()
        plist = load_plist(filename)
        tracks = plist['Tracks']
        for trackId, track in tracks.items():
            description = get_track_description(track)
            track_names.add(description)
        track_name_sets.append(track_names)
    return list(set.intersection(*track_name_sets))

def plot_stats(filename):
    plist = load_plist(filename)
    tracks = plist['Tracks']

    ratings = [x['Album Rating'] for x in tracks.values()]
    durations = [x['Total Time'] for x in tracks.values()]

    if not ratings or not durations:
        print("Sorry, no data in {}".format(filename))
        return

    x = np.array(durations, np.int32)
    x = x/60000
    y = np.array(ratings, np.int32)

    pyplot.subplot(2, 1, 1)
    pyplot.plot(x, y, 'o')
    pyplot.axis([0, 1.05*np.max(x), -1, 110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')

    pyplot.subplot(2,1,2)
    pyplot.hist(x, bins=20)
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')

    pyplot.show()


if __name__ == '__main__':
    plot_stats('test-data/mymusic.xml')
#    print(find_duplicates('test-data/mymusic.xml'))
#    print(find_common_tracks(['test-data/pl1.xml', 'test-data/pl2.xml']))
