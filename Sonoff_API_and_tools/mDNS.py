import sys
import time

from zeroconf import ServiceBrowser, Zeroconf


class MyListener(object):
    """
    This class is used for the mDNS browsing discovery device, including calling the remove_service and add_service
    properties to ServiceBrowser, and also contains broadcasts for querying and updating existing devices.
        Dictionary
        all_info_dict:Qualified device information in the current network     [keys:info.name，val:info]
    """

    def __init__(self):
        self.all_del_sub = []
        self.all_info_dict = {}
        self.all_sub_num = 0
        self.new_sub = False


    def add_service(self, zeroconf, type, name):
        """
        This function is called for ServiceBrowser.This function is triggered when ServiceBrowser finds a new device
        When a subdevice is found, the device information is stored into the all_info_dict
        """
        self.new_sub = True
        print("inter add_service()")
        self.all_sub_num += 1
        info = zeroconf.get_service_info(type, name)
        if info.properties[b'type'] == b'diy_plug':
            self.all_info_dict[name] = info
            if name in self.all_del_sub:
                self.all_del_sub.remove(name)
                print("Service %s added, service info: %s" % (name, info))


def parseAddress(address):
    add_list = []
    for i in range(4):
        add_list.append(int(address.hex()[(i*2):(i+1)*2], 16))
    add_str = str(add_list[0]) + "." + str(add_list[1]) + \
        "." + str(add_list[2]) + "." + str(add_list[3])
    return add_str


def get_device():
    device = []
    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, "_ewelink._tcp.local.", listener=listener)
    # Scan local net for sonoff for 3 seconds
    time.sleep(3)
    zeroconf.close()
    if listener.all_sub_num > 0:
        dicto = listener.all_info_dict.copy()
        for x in dicto.keys():
            info = dicto[x]
            info = zeroconf.get_service_info(info.type, x)
            if info != None:
                device.append([x[8:18], parseAddress(info.address), str(info.port)])
    else:
        print('No device found')
        time.sleep(1)
        sys.exit()
    return device
