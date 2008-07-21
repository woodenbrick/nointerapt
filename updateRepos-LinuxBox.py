#!/usr/bin/env python
import os
import glob
#This is the Linux script which unzips the package lists renames them and replaces the old
#must be run as root

src = '/media/WOODENBRICK/'
file = 'repos.tar'
dest = '/var/lib/apt/lists/'
temp = '/tmp/repos/'
os.system('tar -xvf '+src+'repos.tar -C '+dest)
for item in glob.glob(dest+'*.gz'):
    print 'Unzipping', item
    os.system('gunzip -f '+item)
#os.remove(src+file)


    
