#!/usr/bin/python

import sys

if len(sys.argv) < 2:
  print "usage: %s lista.txt" % sys.argv[0]
  sys.exit(0)

filename = sys.argv[1]

opened = open(filename, 'r')

lowerList = []

for i in opened.readlines():
  low = i.lower()
  lowerList.append(low)

opened.close()

newfile = open('cased.txt', 'a')

for i in lowerList:
  newfile.write(i)

newfile.close() 
