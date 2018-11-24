
import os
from subprocess import call
sourceFile =  r"C:\Users\DOC\PycharmProjects\raw_relink\FILE_LIST_FROM_RESOLVE.txt"
destination  = r'H:\\'
joblist = []





with open(sourceFile, 'r') as abc:
    for i in abc.readlines():
        joblist.append(i.strip())


for each in joblist:
    # print each.strip()
    filename =  os.path.basename(each)
    directory =  os.path.dirname(each)
    # call(["ROBOCOPY"+ " " +directory+" "+destination+' '+ filename + ' /tee /log:_date.txt'])

    call( ["ROBOCOPY"+ " " +directory+" "+destination+' '+ filename + ' /MT:32 '])






