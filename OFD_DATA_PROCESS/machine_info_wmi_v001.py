from pySMART import DeviceList
import json
import sys
import logging

data = {}
devlist = DeviceList()
drive_list = []


print devlist.devices
for i in devlist.devices:
    drive_list.append(i)

data['Model Number'] = 8


json_data = json.dumps(data)
print json_data











# for i in drive_list:
#     if i.assessment != 'PASS':
#         data['Model Number'] = str(i.model)
#         sys.stdout = open('D:\log.txt', 'w')  #to print all the following lines to a text file.
#         print 'Model Number : ' + str(i.model)
#         print 'Capacity : ' +i.capacity
#         print 'supports Smart Status : ' + str(i.supports_smart)
#         print 'Self_Assessment_Status : ' + str(i.assessment)
#         print ''
#         print ('--'*50)
#         print ('--' * 50)
#         print ''
#         print i.attributes[5]
#         print i.attributes[187]
#         print i.attributes[188]
#         print i.attributes[197]
#         print i.attributes[193]
#         print i.attributes[198]
#         print ''
#         print ('--'*50)
#         print ('--' * 50)
#         print ''
#         for each_Attr in i.attributes:
#             if each_Attr != None :
#                 print each_Attr
#         print ''
#         print ('--'*50)
#         print ('--' * 50)
#         print ''
#     else:
#         print 'Model Number : ' + str(i.model) + ' is performing all right.'










