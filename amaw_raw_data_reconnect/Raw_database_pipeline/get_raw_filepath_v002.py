#To copy_raw_data_for_resolve

import sys
import re
import os
import shutil

txt_source_folder = r'J:\Raw_database_pipeline\_Assets'
txtfile = r"C:\Users\DOC\Desktop\raw_pipeline\xml_file_name_list.txt"
mov_file_list = []
mxf_file_list = []
collated_list = []
root_location = r'\\Backup\b4'

def process_txt(txt_arg0):
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
##                    mxf_file_list.append(os.path.join(dirpath,i))


##print mxf_file_list


def Get_mxf_path(source_name,raw_list):
##    print source_name
    for eachfile in raw_list:
        if source_name in eachfile:
##            print eachfile
            collated_list.append(eachfile)


for i in mov_file_list:
    Get_mxf_path(i,mxf_file_list)


##def execute_robocopy(path):
##    shutil.copyfile(path , r'K:\raw_data')
##    print path
##
for abd in collated_list:
    print abd
##    execute_robocopy(abd)











##\\Backup\b1\RAW\16_02_2017\CARD_51\A051R1E3\A051C016_170216_R1E3.mxf\
##The directory name is invalid.