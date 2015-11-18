#! /usr/bin/python3

import csv

videotypes = []

with open('videotypes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        videotypes.append({'type': row['types'], 'dir': row['dir'], 'Count': row['count'],
            'Prefix': row['prefix'], 'openclose': row['openclose']})
        
for video in videotypes:
    print(video)