import json
from pySMART import DeviceList
import time
import os
import requests

date_time = (time.strftime('%Y%m%d_%H%M'))
machine_name = os.environ['COMPUTERNAME']

info = []

devlist = DeviceList()
drive_list = []

for i in devlist.devices:
    drive_list.append(i)

for i in drive_list:
    data = {}
    data = {'Serial Number': str(i.serial), 'Model Number': i.model, 'Capacity': i.capacity,
            'supports Smart Status': i.supports_smart,
            'Self_Assessment_Status': i.assessment}
    try:
        data[i.attributes[1].name] = i.attributes[1].value
        data[i.attributes[3].name] = i.attributes[3].value
        data[i.attributes[4].name] = i.attributes[4].value
        data[i.attributes[5].name] = i.attributes[5].value
        data[i.attributes[7].name] = i.attributes[7].value
        data[i.attributes[9].name] = i.attributes[9].value
        data[i.attributes[10].name] = i.attributes[10].value
        data[i.attributes[12].name] = i.attributes[12].value
        data[i.attributes[184].name] = i.attributes[184].value
        data[i.attributes[187].name] = i.attributes[187].value
        data[i.attributes[188].name] = i.attributes[188].value
        data[i.attributes[189].name] = i.attributes[189].value
        data[i.attributes[190].name] = i.attributes[190].value
        data[i.attributes[191].name] = i.attributes[191].value
        data[i.attributes[192].name] = i.attributes[192].value
        data[i.attributes[193].name] = i.attributes[193].value
        data[i.attributes[194].name] = i.attributes[194].value
        data[i.attributes[195].name] = i.attributes[195].value
        data[i.attributes[196].name] = i.attributes[196].value
        data[i.attributes[197].name] = i.attributes[197].value
        data[i.attributes[198].name] = i.attributes[198].value
        data[i.attributes[199].name] = i.attributes[199].value

    except AttributeError as err:
        pass
        # print(err.args)
    info.append(data)

    # info [each.serial] = each
# print data
# for i in info:
#     print i

json_str = json.dumps(info)

with open(str(machine_name) + '_' + str(date_time) + '.json', 'w') as f:
    json.dump(info, f)
    print "json created"


mydata = info

path = 'http://internal.onefineday.co.in/json.php'  # the url you want to POST to

r = requests.post(path, json=mydata)
print(r.text)
