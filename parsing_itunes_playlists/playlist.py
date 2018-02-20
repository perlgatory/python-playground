import plistlib
from collections import Counter
import numpy as np
from matplotlib import pyplot
import argparse


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

    sufficiently_informed_tracks = [x for x in tracks.values() if ('Album Rating' in x) and ('Total Time' in x)]

    ratings = [x['Album Rating'] for x in sufficiently_informed_tracks]
    durations = [x['Total Time'] for x in sufficiently_informed_tracks]

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

def main():
    #create parser
    desc_str = """
    This program analyzes playlist files (.xml) exported from iTunes."""

    #parse args
    parser =  argparse.ArgumentParser(description=desc_str)
    #add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()

    #add expected arguments
    group.add_argument('--common', nargs='*', dest='plFiles', help='Find common tracks between files',  required=False)
    group.add_argument('--stats', dest='plFile', required=False)
    group.add_argument('--dup', dest='plFileD', required=False)

    #parse args
    args = parser.parse_args()

    if args.plFiles:
        #find common tracks
        for line in find_common_tracks(args.plFiles):
            print(line)
    elif args.plFile:
        #plot stats
        plot_stats(args.plFile)
    elif args.plFileD:
        #find duplicate tracks
        for line in find_duplicates(args.plFileD):
            print(line)
    else:
        print("These are not the tracks you are looking for.")


if __name__ == '__main__':
    main()
