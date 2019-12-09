#################################
#                               #
#       Author: Dave0x21        #
#           Sonoff Menù         #
#                               #
#################################


# Menù


def header(device):
    """
    Print the header of the menù
    """

    device = 'Connected Device: ' + device
    print(r'╔════════════════════════════════════════════════════════════════════════╗')
    print(r'║  ___  ___  _  _  ___  ___ ___   ___ _____   __  __  __  ___  ___  ___  ║')
    print(r'║ / __|/ _ \| \| |/ _ \| __| __| |   \_ _\ \ / / |  \/  |/ _ \|   \| __| ║')
    print(r'║ \__ \ (_) | .` | (_) | _|| _|  | |) | | \ V /  | |\/| | (_) | |) | _|  ║')
    print(r'║ |___/\___/|_|\_|\___/|_| |_|   |___/___| |_|   |_|  |_|\___/|___/|___| ║')
    print(r'║                                                                        ║')
    print(r'║                            Author: Dave0x21                            ║')
    print(r'║                     Release: 0.2  Date: 12/06/2019                     ║')
    center(device)
    print(r'╠════════════════════════════════════════════════════════════════════════╣')
    print(r'║                                                                        ║')


def main(device):
    """
    Print the main meù
    """

    # Check if the device have a saved name
    if len(device) == 4:
        header(device[3])
    else:
        header(device[0])

    print(r'║                               Main Menù                                ║')
    print(r'║                                                                        ║')
    print(r'║                      Get Info..................01                      ║')
    print(r'║                      Turn On...................02                      ║')
    print(r'║                      Turn Off..................03                      ║')
    print(r'║                      Set Power On State........04                      ║')
    print(r'║                      Set Pulse.................05                      ║')
    print(r'║                      Change WiFi...............06                      ║')
    print(r'║                      Unlock OTA................07                      ║')
    print(r'║                      Flash Firmware............08                      ║')
    print(r'║                      Add Device................09                      ║')
    print(r'║                                                                        ║')
    print(r'║                      Exit.......................0                      ║')
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


def device(device):
    """
    Print the device selection menù
    """

    # No device connected in this menù
    header('None')
    print(r'║                             Select Device                              ║')
    print(r'║                                                                        ║')
    device_list(device)
    print(r'║                                                                        ║')
    print(r'║                      Exit.......................0                      ║')
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


def power_on_state(device):
    """
    Print the power on state menù
    """

    # Check if the device have a saved name
    if len(device) == 4:
        header(device[3])
    else:
        header(device[0])

    print(r'║                             Power On State                             ║')
    print(r'║                                                                        ║')
    print(r'║                      On........................01                      ║')
    print(r'║                      Off.......................02                      ║')
    print(r'║                      Stay......................03                      ║')
    print(r'║                                                                        ║')
    print(r'║                      Back.......................0                      ║')
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


def pulse(device):
    """
    Print the pulse state menù
    """

    # Check if the device have a saved name
    if len(device) == 4:
        header(device[3])
    else:
        header(device[0])

    print(r'║                               Set  Pulse                               ║')
    print(r'║                                                                        ║')
    print(r'║                      On........................01                      ║')
    print(r'║                      Off.......................02                      ║')
    print(r'║                                                                        ║')
    print(r'║                      Back.......................0                      ║')
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


def info(device, info, signal):
    """
    Print the info menù
    """

    # Check if the device have a saved name
    if len(device) == 4:
        header(device[3])
    else:
        header(device[0])

    # Add signal ad ip address to info
    info = {**info, **signal, 'ip address': device[1]}

    print(r'║                                  Info                                  ║')
    print(r'║                                                                        ║')
    options_preparation(info)
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


# Utils


def options_preparation(options):
    """
    Prepare the options to be printed on screen
    options must be a dict: {option: value} 
    """

    # Format options ready for output
    options['pulseWidth'] = str(options['pulseWidth'])
    options['pulse width'] = options.pop('pulseWidth')
    options['ota unlock'] = options.pop('otaUnlock')
    options['signal strength'] = options.pop('signalStrength')

    # For each key in options print the info output
    for key in options:
        string = [key, str(options[key])]
        if len(''.join(string)) != 28:
            i = 28 - len(''.join(string))
        center(string[0] + '.'*i + string[1])


def device_list(device):
    """
    Print the device discovered by mDNS
    """
    
    # Firs device have code = 01
    i = 1

    for elem in device:
        # Check if the device have a saved name
        if len(device) == 4:
            string = elem[3]
        else:
            string = elem[0]
        # Build the output string
        dot_number = 28 - len(string) - len(str(i).zfill(2))
        string = string + '.' * dot_number + str(i).zfill(2)
        center(string)
        i += 1


def center(string):
    """
    Center string inside the app space
    """

    n_space = int((72 - len(string)) / 2)
    space = r' ' * n_space
    print('║' + space + string + space + '║')