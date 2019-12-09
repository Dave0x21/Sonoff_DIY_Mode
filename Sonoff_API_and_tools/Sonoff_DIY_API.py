#################################
#                               #
#       Author: Dave0x21        #
#           Sonoff API          #
#                               #
#################################

import requests


def set_ON(device, timeout=5):
    """
    Set the status of the switch to on
    device must be a list that contain id, ip address and the port for the rest API communication
    Return the code error of the request
    """

    url = 'http://{}:{}/zeroconf/switch'.format(device[1], device[2])
    data = '''{
                    "deviceid": "%s",
                    "data": {
                        "switch": "on"
                    }
                }''' % device[0]
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['error']


def set_OFF(device, timeout=5):
    """
    Set the status of the Sonoff to Off
    device must be a list that contain id, ip address and the port for the rest API communication
    Return the code error of the request
    """

    url = 'http://{}:{}/zeroconf/switch'.format(device[1], device[2])
    data = '''{
                    "deviceid": "%s",
                    "data": {
                        "switch": "off"
                    }
                }''' % device[0]
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['error']


def set_Power_On_State(device, state, timeout=5):
    """
    Set the state of the sonoff at power on
    device must be a list that contain id, ip address and the port for the rest API communication
    state must be a 'stay', 'on' or 'off'
    Return the code error of the request
    """

    POSSIBLE_POWER_ON_STATE = ('stay', 'on', 'off')
    if state in POSSIBLE_POWER_ON_STATE:
        url = 'http://{}:{}/zeroconf/startup'.format(device[1], device[2])
        data = '''{
                        "deviceid": "%s",
                        "data": {
                            "startup": "%s"
                        }
                    }''' % (device[0], state)
        response = requests.post(url, data=data, timeout=timeout).json()
        return response['error']
    else:
        return '1'


def get_Signal_Strenght(device, timeout=5):
    """
    Get the signal strenght of the sonoff
    device must be a list that contain id, ip address and the port for the rest API communication
    Return a dict containing the signal strength {signalStrength: value}
    """

    url = 'http://{}:{}/zeroconf/signal_strength'.format(device[1], device[2])
    data = ''' {
                    "deviceid": "%s",
                    "data": { }
                }''' % device[0]
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['data']


def set_Pulse(device, state, width='500', timeout=5):
    """
    Set the pulse function of the sonoff to on or off, if on is selected the width of the puls must be specified
    device must be a list that contain id, ip address and the port for the rest API communication
    state must be 'on' or 'off'
    width must be in range 500-36000000
    Return the code error of the request
    """

    url = 'http://{}:{}/zeroconf/pulse'.format(device[1], device[2])
    data = '''{
                    "deviceid": "%s",
                    "data": {
                        "pulse": "%s",
                        "pulseWidth": %s
                    }
                }''' % (device[0], state, width)
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['error']


def set_WiFi(device, SSID, password, timeout=5):
    """
    Set a new wifi connection
    device must be a list that contain id, ip address and the port for the rest API communication
    Return the code error of the request
    """

    url = 'http://{}:{}/zeroconf/wifi'.format(device[1], device[2])
    data = '''{
                    "deviceid": "%s",
                    "data": { 
                        "ssid": "%s", 
                        "password": "%s"
                    }
                }''' % (device[0], SSID, password)
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['error']


def Unlock_OTA(device, timeout=5):
    """
    Unlock the OTA function of the sonoff
    device must be a list that contain id, ip address and the port for the rest API communication
    Return the code error of the request
    """

    url = 'http://{}:{}/zeroconf/ota_unlock'.format(device[1], device[2])
    data = '''{
                    "deviceid": "%s",
                    "data": { }
                }''' % device[0]
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['error']


def Flash_OTA(device, url, checksum, timeout=5):
    """
    Flash a new firmware to sonoff
    device must be a list that contain id, ip address and port for rest API communication
    url is the url of new firmware
    checksum is the checksum of new firmware
    Return the code error of the request
    """

    url = 'http://{}:{}/zeroconf/ota_flash'.format(device[1], device[2])
    data = '''{
                    "deviceid": "%s",
                    "data": { 
                        "downloadUrl": "%s", 
                        "sha256sum": "%s"
                    }
                }''' % (device[0], url, checksum)
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['error']


def get_Info(device, timeout=5):
    """
    Get the actual info of sonoff
    device must be a list that contain id, ip address and the port for the rest API communication
    Return the code error of the request
    """

    url = 'http://{}:{}/zeroconf/info'.format(device[1], device[2])
    data = '''{
                    "deviceid": "%s",
                    "data": { }
                }''' % device[0]
    response = requests.post(url, data=data, timeout=timeout).json()
    return response['data']
