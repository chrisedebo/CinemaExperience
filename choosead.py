#! /usr/bin/python3

import os
import re
import random
import csv

#import video types from csv
#types, dir, count, prefix, openclose

settingsfile = 'videotypes.csv'

def getcsvsettings(settingsfile):
    #print('===========Getting Settings==============')
    #print(settingsfile)
    videotypes = []
    with open(settingsfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            videotypes.append({'type': row['types'], 'dir': row['dir'], 'count': row['count'],
                'prefix': row['prefix'], 'openclose': row['openclose']})
    #print('===========Getting Settings==============')
    return videotypes

def selectrandomfiles(vdir,vcount,vprefix):
    "Select random number of files based on searchstr in directory dir"
    #print('===========Selecting Random Files==============')
    #print(vdir + ' ' + vcount + ' ' + ' ' + vprefix)
    if vprefix == '':
        randomfiles = [f for f in os.listdir(vdir) if os.path.isfile(os.path.join(vdir,f))]
    else:
        searchstr = vprefix + '*'
        randomfiles = [f for f in os.listdir(vdir) if re.match(searchstr,f)]
    selectedrandomfiles = random.sample(randomfiles,int(vcount))
    
    #print(selectedrandomfiles)
    #print('===========Selecting Random Files==============')
    return selectedrandomfiles

def selectmatchingfiles(thisprefix,otherprefix,videolist):
    "Select matching files for an existing video list based on the prefix"
    #print('============Selecting matching files==============')
    #print(thisprefix + otherprefix)
    #print(videolist)
    selectedmatchingfiles = []
    for video in videolist:
        selectedmatchingfiles.append(video.replace(otherprefix,thisprefix))

    #print(selectedmatchingfiles)
    #print('============Selecting matching files==============')
    return selectedmatchingfiles

def choosevideos(videotype,selectedvideos,videotypes):
    #print('===========Choosing Videos==============')
    #print(videotype)
    #print(selectedvideos)
    if videotype.get('openclose') == '':
        videolist = selectrandomfiles(
            videotype.get('dir'),
            videotype.get('count'),
            videotype.get('prefix'))
    else:
        othertype = videotype.get('openclose')
        for vtype in videotypes:
            if vtype.get('type') == othertype:
    #            print(vtype)
                videolist = selectmatchingfiles(
                    videotype.get('prefix'),
                    vtype.get('prefix'),
                    selectedvideos[vtype.get('type')])
    
    #print (videolist)
    #print('===========Choosing Videos==============')
    return videolist

def CreatePlaylist():
    print("Creating Playlist")

vtypes = getcsvsettings(settingsfile)
selection = {}
for videotype in vtypes:
    selection[videotype.get('type')]=choosevideos(videotype,selection,vtypes)

for videotype in vtypes:
    print('==========' + videotype.get('type') + '==========')
    print(selection[videotype.get('type')])
