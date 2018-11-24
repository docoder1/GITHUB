#To copy_raw_data_for_resolve

import sys
import re
import os
import shutil


droppedFilePath = r"J:\Raw_database_pipeline\_Assets\raw_file_name_list.txt"
##droppedFilePath = sys.argv[1]
dropped_filename = droppedFilePath.split('\\')[-1]

##txtfile = r"C:\Users\DOC\Desktop\raw_pipeline\xml_file_name_list.txt"
proxy_file_list = []
mxf_file_list = []
bmcc_file_list = []
collated_list = []
root_location = r'\\Backup\b4'


with open(droppedFilePath) as filelist:
    lines = filelist.readlines()
    for each in lines:
        proxy_file_list.append(each.strip('\n'))

for i in proxy_file_list:
    print "proxy data :: "+ i


for dirpath, dirnames, filenames in os.walk(root_location):
        for i in filenames:
            if os.path.splitext(i)[1] == '.mxf':
                print os.path.splitext(i)[0]
##                    print os.path.join(dirpath,i)
##                if os.path.exists(os.path.join(dirpath,i)):
##                    mxf_file_list.append(('ROBOCOPY ' +dirpath +' K:\ '+ i + ' /MT'))
##                   mxf_file_list.append(os.path.join(dirpath,i))


##print mxf_file_list


##def Get_mxf_path(source_name,raw_list):
####    print source_name
##    for eachfile in raw_list:
##        if source_name in eachfile:
####            print eachfile
##            collated_list.append(eachfile)


##for i in mov_file_list:
##    Get_mxf_path(i,mxf_file_list)


##def execute_robocopy(path):
##    shutil.copyfile(path , r'K:\raw_data')
##    print path
##
##for abd in collated_list:
##    print abd
##    execute_robocopy(abd)











##\\Backup\b1\RAW\16_02_2017\CARD_51\A051R1E3\A051C016_170216_R1E3.mxf\
##The directory name is invalid.