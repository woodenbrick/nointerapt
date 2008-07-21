#check if ipod is plugged in, untar the downloads file to the var cache
import os

path = None
if os.path.isfile('/media/WOODENBRICK/downloads.tar'):
    print 'iPod connected, extracting debs to /var/apt/cache/'
    path = '/media/WOODENBRICK/downloads.tar'
    
else:
    print 'iPod not connected, trying desktop...'
    
if path != None:    
    os.system('tar -xvf '+path+' -C /var/cache/apt/archives')
    print 'Done! Use Synaptic to install'
else:
    print 'Path to downloads.tar couldnt be found'