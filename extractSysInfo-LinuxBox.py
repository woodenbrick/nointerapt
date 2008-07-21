#run this script to get a list of repositries that should be downloaded

sysInfo = file('sysInfo', 'w')
aptSources = file('/etc/apt/sources.list', 'r')
#only take online resources, leave local repos, cds etc.
allowedSources = ('http', 'ftp')
sections=[]
for line in aptSources.readlines():
    if line.startswith('deb'):
        x = line.split(' ')
        lenX = len(x)
        url = x[1][x[1].find('/')+2:]
        dist = x[2]
        if allowedSources.__contains__(x[1][0:4]):
            print line
            for i in range(3, lenX-1):
                sysInfo.write(url+'dists/'+dist+'/'+x[i]+'/binary-i386/Packages\n')
sysInfo.close()            
   
#a repo header: http://ftp.bg.debian.org/debian/dists/lenny/contrib/binary-i386/Packages.gz    
#deb http://ftp.bg.debian.org/debian/ lenny main contrib non-free 
#deb http://dl.google.com/linux/deb/ stable non-free

#send to ipod
#genf.moveToFlash('sysInfo')
import os
#os.system('mv sysInfo /media/WOODENBRICK')


