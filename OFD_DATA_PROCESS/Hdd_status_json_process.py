import json
from pySMART import DeviceList

info = {}


devlist = DeviceList()
drive_list = []

for i in devlist.devices:
    drive_list.append(i)

for i in drive_list:
    data = {'Model Number': i.model, 'Capacity': i.capacity, 'supports Smart Status': i.supports_smart,
            'Self_Assessment_Status': i.assessment}
    try:
        data[i.attributes[5].name] = i.attributes[5].value
        data[i.attributes[187].name] = i.attributes[187].value
        data[i.attributes[188].name] = i.attributes[188].value
        data[i.attributes[197].name] = i.attributes[197].value
        data[i.attributes[193].name] = i.attributes[193].value
        data[i.attributes[198].name] = i.attributes[198].value
    except AttributeError as err:
        pass

        # print(err.args)
    info[i.model] = data

json_str = json.dumps(info)

with open('test.json', 'w') as f:
    json.dump(info, f)
    print "json created"
