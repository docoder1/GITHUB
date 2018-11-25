from dirsync import sync
source = r'I:\GITHUB'
dest = r'F:\dest'
mylogger = 'F:\log.txt'
sync(source,dest, 'sync',purge = True , create = True)