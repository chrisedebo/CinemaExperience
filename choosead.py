#! /usr/bin/python3

import os
import re
import random
import csv

#import video types from csv
#types, dir, count, prefix, openclose

settingsfile = 'S:\\Media Library\\Cinema Experience\\videotypes.csv'
#exclude files
exclusions = ['thumbs.db']


def getcsvsettings(settingsfile):
    videotypes = []
    with open(settingsfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            videotypes.append({'type': row['types'], 'dir': row['dir'], 'count': row['count'],
                'prefix': row['prefix'], 'openclose': row['openclose']})
    return videotypes

def selectrandomfiles(vdir,vcount,vprefix):
    "Select random number of files based on searchstr in directory dir"
    if vprefix == '':
        randomfiles = [f for f in os.listdir(vdir) if os.path.isfile(os.path.join(vdir,f)) and 
                f not in exclusions]
    else:
        searchstr = vprefix + '*'
        randomfiles = [f for f in os.listdir(vdir) if re.match(searchstr,f)]
    selectedrandomfiles = random.sample(randomfiles,int(vcount))
    
    return selectedrandomfiles

def selectmatchingfiles(thisprefix,otherprefix,videolist):
    "Select matching files for an existing video list based on the prefix"
    selectedmatchingfiles = []
    for video in videolist:
        selectedmatchingfiles.append(video.replace(otherprefix,thisprefix))

    return selectedmatchingfiles

def choosevideos(videotype,selectedvideos,videotypes):
    if videotype.get('openclose') == '':
        videolist = selectrandomfiles(
            videotype.get('dir'),
            videotype.get('count'),
            videotype.get('prefix'))
    else:
        othertype = videotype.get('openclose')
        for vtype in videotypes:
            if vtype.get('type') == othertype:
                videolist = selectmatchingfiles(
                    videotype.get('prefix'),
                    vtype.get('prefix'),
                    selectedvideos[vtype.get('type')])
    
    return videolist

def CreatePlaylist(videotypes,selection):
    print("Creating Playlist")
    plsfile = open('playlist.pls','w')
    plsfile.write('[playlist]\n\n')
    vcount=0
    for vtype in videotypes:
        videos = selection[vtype.get('type')]
        for video in videos:
            vcount=vcount+1
            plsfile.write("File" + str(vcount) + '=' + vtype.get('dir') + '\\' + video + '\n')
    
    plsfile.write('\n\nNumberofEntries=' + str(vcount) + '\nVersion=2')
    plsfile.close

vtypes = getcsvsettings(settingsfile)
selection = {}
for videotype in vtypes:
    selection[videotype.get('type')]=choosevideos(videotype,selection,vtypes)

for videotype in vtypes:
    print('==========' + videotype.get('type') + '==========')
    print(selection[videotype.get('type')])

CreatePlaylist(vtypes,selection)
