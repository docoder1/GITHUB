#To copy_raw_data_for_resolve

import sys
import re
import os
import subprocess
from subprocess import call
from subprocess import PIPE



txtfile = r"C:\Users\DOC\Desktop\proxy_filelist.txt"
mov_file_list = []
mxf_file_list = []
collated_list = []
root_location = r'\\Backup\b1\RAW'


with open(txtfile) as filelist:
    lines = filelist.readlines()
for each in lines:
    mov_file_list.append(each.strip())


##print mov_file_list

##for root,dirs,files in os.walk(root_location):
##    for i in dirs:
##        folder_path = os.path.join(root,i,)
##        if os.path.exists(folder_path):
##            os.path.join(folder_path,files)



for dirpath, dirnames, filenames in os.walk(root_location):
        for i in filenames:
            if os.path.splitext(i)[1] == '.mxf':
                if os.path.exists(os.path.join(dirpath,i)):
                    mxf_file_list.append(('ROBOCOPY ' +dirpath +' K:\ '+ i + ' /MT'))


##print mxf_file_list


def Get_mxf_path(source_name,raw_list):
##    print source_name
    for eachfile in raw_list:
        if source_name in eachfile:
##            print eachfile
            collated_list.append(eachfile)


for i in mov_file_list:
    Get_mxf_path(i,mxf_file_list)


def execute_robocopy(path):
    cmd = r'ROBOCOPY {} {} {}'.format(path)
    p = subprocess.Popen(cmd,stderr=PIPE,stdout=PIPE)
    a = p.communicate()
    for i in a:
        print i
##    call(path)
##    print path
##
for abd in collated_list:
    print abd
    execute_robocopy(abd)











##\\Backup\b1\RAW\16_02_2017\CARD_51\A051R1E3\A051C016_170216_R1E3.mxf\
##The directory name is invalid.