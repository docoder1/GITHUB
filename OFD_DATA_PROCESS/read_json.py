import json

with open('DOC_20181126_1829.json', 'r') as f:
    data = json.load(f)

# print data

for i in data:
    print i
    # for k,v in i.items():
    #     print k
    #     print v
    # print type(i)

# for k,v in data.items():
#     print k
#     print v

