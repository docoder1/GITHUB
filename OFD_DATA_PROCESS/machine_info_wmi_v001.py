from pySMART import DeviceList
devlist = DeviceList()
x = xrange(1,)
# print devlist.devices
for i in devlist.devices:
    print i.name
    print i.supports_smart
    print i.is_ssd
    print i.run_selftest



# for i in devlist.devices:
#     print i.device()
#     print i.attributes[3]
#     print i.assessment



