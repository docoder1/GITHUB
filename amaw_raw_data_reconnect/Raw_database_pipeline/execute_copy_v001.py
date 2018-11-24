import re
import sys
import os

root_server = r'\\Backup\b1'

source_list = r"J:\Raw_database_pipeline\_Assets\xml_file_name_list.txt"
file_list = []
mxf_list = []
destination = 'K:\\'

with open (source_list) as Alist:
    for i in Alist:
        file_list.append(i.strip('\n'))

print file_list

##for dirpath, dirnames, filenames in os.walk(root_server):
##    concat_folder = os.path.join(root_server,dirpath)
##    for i in filenames:
##        stripped_name =os.path.splitext(i)[0]
##        print stripped_name
##        if stripped_name in file_list:
####            print ' check ' + os.path.join(dirpath,i)
##            if os.path.exists(os.path.join(dirpath,i)):
####                print os.path.splitext(i)[0] + ' :::: '+ dirpath
##                robocopy_command = concat_folder + ' ' + destination + ' ' + stripped_name + ' ' + '/MT'
##                print robocopy_command




##        fname, fext = os.path.splitext(each_file)
##        print type(fname)
##        if fext == '.mxf':
##            mxf_list.append(fname)
##            print fname

##        if i in mxf_list:
##            print dirpath


##    for each_file in filenames:
##        name, ext = os.path.splitext(each_file)
##        count = 0
##        if ext == '.mxf':
####            count += 1
##            print len(name)
##            print count
