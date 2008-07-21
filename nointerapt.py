#!/usr/bin/env python
import os
import glob

#static variables, these should be set by another script

#for linux
FLASH = '/media/WOODENBRICK/'
REPO_LIST_TAR = 'repos.tar'
DEB_TAR = 'downloads.tar'
REPO_LISTS = '/var/lib/apt/lists/'
DEB_CACHE = '/var/cache/apt/archives/'
LOCAL_REPOS = ['/media/hda1/repo/all/', '/media/hda1/repo/amd64/']
APT_MARKINGS = '/home/wode/aptMarkings'
DESKTOP = '/home/wode/Desktop/'
DOWNLOAD_LIST = 'downloadList'
SYS_INFO = '/home/wode/programming/sysInfo'

def updateRepositries():
    '''Copies the repo packages.gz and release files to the apt/lists and unzips'''

    os.system('tar -xvf ' + FLASH + REPO_LIST_TAR + ' -C ' + REPO_LISTS)
    for item in glob.glob(REPO_LISTS + '*.gz'):
        print 'Unzipping', item
        os.system('gunzip -f ' + item)
    os.remove(FLASH + REPO_LIST_TAR)




def addDebs():
    '''Adds any debs from the download.tar to the repositry'''

    if os.path.isfile(FLASH + DEB_TAR):
        print 'iPod connected, extracting debs to /var/cache/'
        os.system('tar -xvf ' + FLASH + DEB_TAR + ' -C ' + DEB_CACHE)
        print 'Done! Use Synaptic to install'
        
    else:
        print 'Path to ', DEB_TAR, 'could not be found'
    
    
    
def readMarkings():
    '''Returns a list of items to be installed by reading a synapic markings list'''
   
    packageList = open(APT_MARKINGS, 'r')
    packages = []
    for line in packageList.readlines():
        f = line.split('\t')
        if f[2]=="install\n":
            packages.append(f[0])
    packageList.close()
    return packages

def checkWanted(line, packages):
    '''Checks if this package is desired for download'''
    for package in packages:
        if line.split(' ')[1] == package+'\n':
            print 'Retrieving url for', package
            return True
    return False
       

def inCache(pkg, downloadList):
    '''Checks if package already exists in a local cache or repositry'''
    
    url = pkg.split(' ')
    pkgName = str(pkg[pkg.rfind('/')+1:-1])
    #check local cache first
    if os.path.isfile(DEB_CACHE + pkgName):
        print 'pkgName already exists in cache, skipping'
        return
    else:
        for repo in LOCAL_REPOS:
            if os.path.isfile(repo + pkgName):
                print pkgName, 'is in a local repositry, moving to cache...'
                os.system('mv ' + repo + pkgName + ' ' + DEB_CACHE)
                return
    downloadList.write('ftp.bg.debian.org/debian/'+url[1])
        
    

def generateDownloadList():
    downloadList = file(DESKTOP + DOWNLOAD_LIST, 'w')
    repos = file(SYS_INFO, 'r')
    packages = readMarkings()
    for r in repos.readlines():
        repoName = REPO_LISTS + r.replace('/', '_')[0:-1] #get the file name of each repositry list
        f = file(repoName, 'r')
        for line in f.readlines():
            if line.startswith('Package:'):
                getUrl = checkWanted(line, packages)
            if line.startswith('Filename:') and getUrl == True:
                print 'adding', line
                inCache(line, downloadList)
                getUrl = False

    print 'download list complete'
    downloadList.close()
    #os.system('mv ' + downloadList + ' ' + FLASH)
def testCheckout():
    print 'ass'