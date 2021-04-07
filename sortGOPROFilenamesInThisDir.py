#!/usr/bin/env python

import os
from os import listdir
from os.path import isfile, join


mypath = os.getcwd()
i = 0

directoryListing = listdir(mypath)
directoryListing.sort()

for f in directoryListing:
 fullPathName = join(mypath, f)

 if isfile(fullPathName):
  if f[0:4] == 'GOPR':
   print(f[4:len(f) - 4] + '00.MP4')
   os.rename(f, f[4:len(f) - 4] + '00.MP4')

  elif f[0:2] == 'GP':
   print(f[4:len(f) - 4] + f[2:4] + '.MP4')
   os.rename(f, f[4:len(f) - 4] + f[2:4] + '.MP4')

#os.rename(f, newFileName)
#for f in files:
#    print(f[5:7]+'.'+f[9:11])
#    os.rename(f, f[5:7] + '.' + f[9:11] + '.mp')
