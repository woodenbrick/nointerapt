import nointerapt

print 'Enter repo, gen or adddeb'
inp = raw_input()
if inp == 'repo':
    nointerapt.updateRepositries()
elif inp == 'gen':
    nointerapt.generateDownloadList()
elif inp == 'adddeb':
    nointerapt.addDebs()
else:
    print 'invalid option'