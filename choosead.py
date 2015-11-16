#! /usr/bin/python3

import os
import re
import random

#Video types, directories, count of type and prefix for two part 
videos = [{'type':'PDOpen',   'dir' : 'PearlandDeanIdents', 'Count' : 1, 'Prefix': 'Opening_'},
        [{'type':'Ads',       'dir' : 'Adverts',            'Count' : 5, 'Prefix': None},
        [{'type':'PDClose',   'dir' : 'PearlandDeanIdents', 'Count' : 1, 'Prefix': 'Close_'},
        [{'type':'CineID',    'dir' : 'CinemaIdents',       'Count' : 1, 'Prefix': None},
        [{'type':'InHouseAds','dir' : 'InHouseAdverts',     'Count' : 2, 'Prefix': None},
        [{'type':'Prev',      'dir' : 'Previews',           'Count' : 1, 'Prefix': None},
        [{'type':'Tr',        'dir' : 'Trailers',           'Count' : 1, 'Prefix': None},
        [{'type':'CineP',     'dir' : 'CinemaPolicy',       'Count' : 1, 'Prefix': None},
        [{'type':'FP',        'dir' : 'FeaturePresentation','Count' : 1, 'Prefix': None},




#Video types and directories they are stored in
videodirtypes = {'PDOpen': 'PearlandDeanIdents', 'Ads': 'Adverts', 
    'PDClose': 'PearlandDeanIdents', 'CineId': 'CinemaIdents', 'InHouseAds': 'InHouseAdverts',
    'Prev': 'Previews', 'Tr': 'Trailers', 'CineP': 'CinemaPolicy', 'FP': 'FeaturePresentation'}

#Video order count
videocount = [{'PDOpen': 1}, 'Ads': 5, 'PDClose': 1, 'CineId': 1, 'InHouseAds': 2, 
    'Prev': 1, 'Tr': 3, 'CineP': 1, 'FP': 1}]

#Videos with a prefix for open/close
prefixtypes = {'PDopen': 'Opening_', 'PDClose': 'Closing_'}


def selectrandomfiles(vdir,vcount,vprefix = None):
	"Select random number of files based on searchstr in directory dir"
    if vprefix == None
        searchstr = '*'
    else
        searchstr = vprefix + '*'

	randomfiles = [f for f in os.listdir(dir) if re.match(searchstr,f)]
	selectedrandomfiles = random.sample(randomfiles,noofitems)

	return selectedrandomfiles

def printvideos(videos):
	for videotype, videolist in videos.items():
		print("=====" + videotype + "=====")
		print("\n".join(videolist))

def CreatePlaylist()
    Print "Creating Playlist"

def choosevideos(videotype):
    searchstr = openclosetypes.get(videotype)
    
