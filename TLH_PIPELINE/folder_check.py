import sys
import re
import os


folder_repo =  'D:\TLH_CLIMAX\CARD_01'

folder_list = os.listdir(folder_repo)

# print folder_list

def getFrames(path):
    frames = os.listdir(path)
    print path +' : '+ str(len(frames))


for i in folder_list:
    getFrames(folder_repo+'/'+i)
