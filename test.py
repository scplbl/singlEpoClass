import load_save as ls
import glob

filesDir = '/Users/carolinesofiatti/projects/classification/data/test/'
oldFiles = sorted(glob.glob(filesDir + 'original/*simulated*.gz'))
newFiles = sorted(glob.glob(filesDir + 'check/*simulated*.gz'))

for i, oldFile in enumerate(oldFiles):
    oldDict = ls.load(oldFiles[i])
    newDict = ls.load(newFiles[i])
    if oldDict != newDict:
        print '**Failure to rebuild, new MC file is different from old.'
    else:
        print 'OK'
