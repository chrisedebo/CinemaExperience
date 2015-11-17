#! /usr/bin/python3

import os
import re
import random
import csv

#import video types from csv
#types, dir, count, prefix, openclose

settingsfile = 'videotypes.csv'

def getcsvsettings(settingsfile):
    print(settingsfile)
    videotypes = []
    with open(settingsfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            videotypes.append({'type': row['types'], 'dir': row['dir'], 'count': row['count'],
                'prefix': row['prefix'], 'openclose': row['openclose']})
    return videotypes

def selectrandomfiles(vdir,vcount,vprefix):
    "Select random number of files based on searchstr in directory dir"
    print(vdir + vcount + vprefix)
    if vprefix == '':
        randomfiles = [f for f in os.listdir(vdir) if isfile(join(vdir,f))]
    else:
        searchstr = vprefix + '*'
        randomfiles = [f for f in os.listdir(vdir) if re.match(searchstr,f)]
    selectedrandomfiles = random.sample(randomfiles,int(vcount))
    
    return selectedrandomfiles

def selectmatchingfiles(thisprefix,otherprefix,videolist):
    "Select matching files for an existing video list based on the prefix"
    print(thisprefix + otherprefix)
    print(videolist)
    selectedmatchingfiles = []
    for video in videolist.items():
        selectedmatchingfiles.append(video.replace(otherprefix,thisprefix))

    return selectedmatchingfiles

def choosevideos(videotype,selectedvideos):
    print(videotype)
    print(selectedvideos)
    if videotype.get('openclose') == '':
        videolist = selectrandomfiles(
            videotype.get('dir'),
            videotype.get('count'),
            videotype.get('prefix'))
    else:
        othertype = videotype.get('openclose')
        for vtype in videotypes.items():
            if vtype.get('type' == othertype):
                    videolist = selectmatchingfiles(
                        videotype.get('prefix'),
                        vtype.get('prefix'),
                        selectedvideos[vtype.get('type')])
    return videolist

def CreatePlaylist():
    print("Creating Playlist")

vtypes = getcsvsettings(settingsfile)
selection = {}
for videotype in vtypes:
    selection[videotype.get('type')]=choosevideos(videotype,selection)

print(selection)
