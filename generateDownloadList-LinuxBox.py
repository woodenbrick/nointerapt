#This will generate a list of packages to be downloaded by using a synapic markings download file
import os
dest = '/media/WOODENBRICK/'

packageList = open('/home/wode/aptMarkings', 'r')
packages = []
for line in packageList.readlines():
    f = line.split('\t')
    if f[2]=="install\n":
        packages.append(f[0])
packageList.close()


downloadList = '/home/wode/Desktop/downloadList'
urlFile = file(downloadList, 'w')
section = ['main', 'contrib', 'non-free']

varDir = '/var/lib/apt/lists/'
repos = file('sysInfo', 'r')
for r in repos.readlines():
    #break out of loop if there is nothin left in the packages[] <=to do
    fulldir = varDir + r.replace('/', '_')[0:-1]
    f = file(fulldir, 'r')
    getUrl = False
    for line in f.readlines():
        if line.startswith('Package:'):
            for package in packages:
                if line.split(' ')[1] == package+'\n':
		    print 'Retrieving url for', package
                    getUrl = True
        if line.startswith('Filename:') and getUrl == True:
	    #check to make sure the package is not in any cache
	    url = line.split(' ')
	    filename = str(line[line.rfind('/')+1:-1])
	    if os.path.isfile('/var/cache/apt/archives/'+filename):
		print 'File already exists in cache, skipping'
            elif os.path.isfile('/media/hda3/var/cache/apt/archives/'+filename):
	        print 'Url exists in old cache, excluding from download list'
		os.system('mv /media/hda3/var/cache/apt/archives/'+filename+' /var/cache/apt/archives/')
	    else:
		urlFile.write('ftp.bg.debian.org/debian/'+url[1])
            getUrl = False

print 'download list complete'
urlFile.close()
os.system('mv '+downloadList+' '+dest)
