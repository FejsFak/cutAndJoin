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

#----------------------FORMAT PLIKU czasy.dat----------------------#
#                                                                  #
#   W celu określenia przedziałów materiału video, które mają      #
#   zostać poddane obróbce należy podać zakresy czasu <od>-<do>    #
#   w fomacie HH:mm:ss-HH:mm:ss dla każdego kawałka filmu o        #
#   normalnej prędkości (np. 00:00:15-1:03:47) oraz w formacie     #
#   tHH:mm:ss-HH:mm:ss dla fragmentów filmu które mają być         #
#   przyśpieszone (np. t1:03:47-02:13:70). Kolejne zakresy czasów  #
#   wpisujemy jeden pod drugim. Ważne jest aby nie popełniać       #
#   błędów ponieważ program w tym momencie nie posiada żadnej      #
#   funkcji sprawdzania poprawności składni dla danych z pliku     #
#   więc po napotkaniu błędnego zapisu po prostu się wysypie.      #
#                                                                  #
#------------------------------------------------------------------#

text_file = open(join(mypath, 'czasy.dat'), 'r')
lines = text_file.readlines()

fullPathName = join(mypath, 'joinOutput.mkv')

if isfile(fullPathName):
  i = i + 1
  for czas in lines:
    cz = czas.rstrip().split('-')

    if not cz:
      break
    t = 0

    if cz[0][0] == 't':
      t = 1
      cz[0] = cz[0][1:len(cz[0])]

    x1 = time.strptime(cz[0],'%H:%M:%S')
    s1 = datetime.timedelta(hours=x1.tm_hour,minutes=x1.tm_min,seconds=x1.tm_sec).total_seconds()

    x2 = time.strptime(cz[1],'%H:%M:%S')
    s2 = datetime.timedelta(hours=x2.tm_hour,minutes=x2.tm_min,seconds=x2.tm_sec).total_seconds()

    s = str(int(s2 - s1))
    newFilename = str(j) + '.mp4'
    j = j + 1

    args = ' -i ' + fullPathName + ' -ss ' + cz[0] + ' -t ' + s + ' -vcodec copy -acodec copy ' + newFilename
    subprocess.call('ffmpeg' + args, shell=True)

    if t:
      args = ' -i ' + newFilename + ' -filter_complex "[0:v]setpts=0.0625*PTS[v];[0:a]atempo=2.0,atempo=2.0,atempo=2.0,atempo=2.0[a]" -map "[v]" -map "[a]" timelaps_' + newFilename
      subprocess.call('ffmpeg' + args, shell=True)

    subprocess.call('ffmpeg' + args, shell=True)

    if t:
      args = ' -i ' + newFilename + ' -filter_complex "[0:v]setpts=0.125*PTS[v];[0:a]atempo=2.0,atempo=2.0,atempo=2.0[a]" -map "[v]" -map "[a]" timelaps_' + newFilename
      subprocess.call('ffmpeg' + args, shell=True)
      os.replace('timelaps_' + newFilename, newFilename)

fileList = ''
filterComplex = ''

k = 1
while k < j:
  filterComplex += '[' + str(k - 1) + ':v:0][' + str(k - 1) + ':a:0]'
  fileList += ' -i ' + str(k) + '.mp4'
  k += 1

ffmpeg = 'ffmpeg' + fileList + ' -filter_complex "' + filterComplex + 'concat=n=' + str(k - 1) + ':v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" newMovie.mkv'
subprocess.call(ffmpeg, shell=True)
