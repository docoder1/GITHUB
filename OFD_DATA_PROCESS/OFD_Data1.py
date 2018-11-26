# -------------------------------------------------------------------------------
# Name:        mechanism for getting a list of removable hard drives.
# Purpose:     To get system status for all the machines on network.
## Author:     DOC
#
# Created:     18/10/2018
# Copyright:   (c) DOC 2018
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import os
import win32api
import platform
import matplotlib.pyplot as plt


#GET SYSTEM SPECIFIC INFORMATION
machine_name = os.environ['COMPUTERNAME']
os = platform.platform()
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print os
print machine_name

win32api.Beep(500,50)

def size_calculations(value):
    # 2**10 = 1024
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while value > power:
        value /= power
        n += 1
    return value




#Function to calculate size on disk
def bytes_2_human_readable(number_of_bytes):
    if number_of_bytes < 0:
        raise ValueError("!!! number_of_bytes can't be smaller than 0 !!!")

    step_to_greater_unit = 1024.

    number_of_bytes = float(number_of_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes)






def get_free_space (letter):
    size = win32api.GetDiskFreeSpaceEx(letter)
    free_bytes = size[0]
    total_space = size[1]
    return  free_bytes, total_space



for each_drive in drives:
    print each_drive
    freebytes , total_Space = get_free_space(each_drive)
    free_space = bytes_2_human_readable(freebytes)
    total_space_tb = bytes_2_human_readable(total_Space)
    print free_space
    print total_space_tb






# slices_hours = [4, 8]
# activities = ['Free Space', 'Total Space']
# colors = ['r', 'g']
# plt.pie(slices_hours, labels=activities, colors=colors, startangle=float(total_space), autopct='%.1f%%')
# plt.show()

