import os
import re
import sys
import shutil
import time
import random


then = time.time() #Time before the operations start

source_path = r'C:\Users\DOC\Downloads'
dest_path = r'F:\AUTOMATED_DOWNLOADS'
avoid_ext = ['.crdownload' , '.ini' ]

#to get a list of stray files from a given folder
#it returns a proper filelist with path which can be given to os module

def get_file_list(path):
    """

    :param path:
    :return:
    """
    filelist = []
    unc_filelist = []
    flist = os.listdir(path)
    for each in flist:
        if os.path.isfile(os.path.join(path,each)):
            name, ext = os.path.splitext(os.path.join(path,each))
            if not ext == '':
                if not ext in avoid_ext:
                    # print ext
                    unc_filelist.append(each)

    return (unc_filelist)


# print get_file_list(source_path)

#this gives back name ahe extension of the file
def get_extension(file_path):
    """

    :param file_path:
    :return:
    """
    name, ext = os.path.splitext(file_path)
    if not ext in avoid_ext:
        return (name,ext.split('.')[1])



def create_folders(ext):
    """

    :param ext:
    :return:
    """
    new_folder = []
    if not ext in avoid_ext:
        temp_path = os.path.join(dest_path,ext)
        if not os.path.exists(temp_path):
            new_folder.append(temp_path)
            os.makedirs(temp_path)
    return new_folder


#this function takes filename and destination folder to concat final path and move files
def organize_files(filename, destfolder):
    """

    :param filename:
    :param destfolder:
    """
    source = os.path.join(source_path,filename)
    dest = os.path.join(destfolder, filename )
    print source
    shutil.move(source,dest)
    print dest





for ind_file in get_file_list(source_path):
    name, ext = get_extension(os.path.join(source_path,ind_file))
    create_folders(ext)
    dest_folder = os.path.join(dest_path,ext)
    print dest_folder
    organize_files(ind_file,dest_folder )
    # print ind_file
    # print ext





now = time.time() #Time after it finished

print("It took: ", now-then, " seconds")
