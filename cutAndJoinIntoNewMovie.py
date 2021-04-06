#!/usr/bin/env python

import os
from os import listdir
from os.path import isfile, join
import subprocess
import datetime
import time

mypath = os.getcwd()
i = 0
j = 1

directoryListing = listdir(mypath)
directoryListing.sort()

text_file = open(join(mypath, 'czasy.dat'), 'r')
lines = text_file.readlines()

fullPathName = join(mypath, 'joinOutput.mkv')

if isfile(fullPathName):
  i = i + 1
  for czas in lines:
    cz = czas.rstrip().split('-')
    #print(cz)
    if not cz:
      break
    t = 0
    if cz[0][0] == 't':
      t = 1
      cz[0] = cz[0][1:len(cz[0])]

    #print(cz)
    x1 = time.strptime(cz[0],'%H:%M:%S')
    s1 = datetime.timedelta(hours=x1.tm_hour,minutes=x1.tm_min,seconds=x1.tm_sec).total_seconds()

    x2 = time.strptime(cz[1],'%H:%M:%S')
    s2 = datetime.timedelta(hours=x2.tm_hour,minutes=x2.tm_min,seconds=x2.tm_sec).total_seconds()

    s = str(int(s2 - s1))

    newFilename = str(j) + '.mp4'
    j = j + 1

    args = ' -i ' + fullPathName + ' -ss ' + cz[0] + ' -t ' + s + ' -vcodec copy -acodec copy ' + newFilename
    #print(args)

    subprocess.call('ffmpeg' + args, shell=True)

    if t:
      #args = ' -i ' + newFilename + ' -filter:v "setpts=0.04*PTS" timelaps_' + newFilename
      args = ' -i ' + newFilename + ' -filter_complex "[0:v]setpts=0.125*PTS[v];[0:a]atempo=2.0,atempo=2.0,atempo=2.0[a]" -map "[v]" -map "[a]" timelaps_' + newFilename
      print(args)

      subprocess.call('ffmpeg' + args, shell=True)

      os.replace('timelaps_' + newFilename, newFilename)

fileList = ''
filterComplex = ''

k = 0
while k < j:
  filterComplex += '[' + str(k) + ':v:0][' + str(k) + ':a:0]'
  k += 1
  fileList += ' -i ' + str(k) + '.mp4'

subprocess.call('ffmpeg' + fileList + '-filter_complex "' + filterComplex + 'concat=n=' + str(k) + ':v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" newMovie.mkv', shell=True)

#ffmpeg -i input1.mp4 -i input2.webm -i input3.mov \
#-filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0][2:v:0][2:a:0]concat=n=3:v=1:a=1[outv][outa]" \
#-map "[outv]" -map "[outa]" output.mkv

