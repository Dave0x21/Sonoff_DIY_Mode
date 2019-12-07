#################################
#                               #
#       Author: Dave0x21        #
#           Sonoff Menù         #
#                               #
#################################

def center(string):
    n_space = int((72 - len(string)) / 2)
    space = r' ' * n_space
    print('║' + space + string + space + '║')


def header(device):
    device = 'Connected Device: ' + device
    print(r'╔════════════════════════════════════════════════════════════════════════╗')
    print(r'║  ___  ___  _  _  ___  ___ ___   ___ _____   __  __  __  ___  ___  ___  ║')
    print(r'║ / __|/ _ \| \| |/ _ \| __| __| |   \_ _\ \ / / |  \/  |/ _ \|   \| __| ║')
    print(r'║ \__ \ (_) | .` | (_) | _|| _|  | |) | | \ V /  | |\/| | (_) | |) | _|  ║')
    print(r'║ |___/\___/|_|\_|\___/|_| |_|   |___/___| |_|   |_|  |_|\___/|___/|___| ║')
    print(r'║                                                                        ║')
    print(r'║                            Author: Dave0x21                            ║')
    print(r'║                     Release: 0.1  Date: 12/06/2019                     ║')
    center(device)
    print(r'╠════════════════════════════════════════════════════════════════════════╣')
    print(r'║                                                                        ║')


def main(device):
    header(device[0])
    print(r'║                               Main Menù                                ║')
    print(r'║                                                                        ║')
    print(r'║                      Get Info..................01                      ║')
    print(r'║                      Turn On...................02                      ║')
    print(r'║                      Turn Off..................03                      ║')
    print(r'║                      Set Power On State........04                      ║')
    print(r'║                      Get Signal Strenght.......05                      ║')
    print(r'║                      Set Pulse.................06                      ║')
    print(r'║                      Change WiFi...............07                      ║')
    print(r'║                      Unlock OTA................08                      ║')
    print(r'║                      Flash Firmware............09                      ║')
    print(r'║                                                                        ║')
    print(r'║                      Exit.......................0                      ║')
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


def device(device):
    header('None')
    print(r'║                             Select Device                              ║')
    print(r'║                                                                        ║')
    device_list(device)
    print(r'║                                                                        ║')
    print(r'║                      Exit.......................0                      ║')
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


def device_list(device):
    i = 1
    for elem in device:
        n_space = int((72 - len('{}.................{}'.format(elem[0], i))) / 2)
        space = r' ' * n_space
        print(r'║' + space + r'{}.................{}'.format(elem[0], i) + space + r'║')
        i += 1


def power_on_state(device):
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

def info(device, info):
    info = options_preparation(info, info=True)
    header(device[0])
    print(r'║                                  Info                                  ║')
    print(r'║                                                                        ║')
    for elem in info:
        print(r'║                      {}                      ║'.format(elem))
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')


def options_preparation(options, info=False):
    formatted_options = []
    options = eval(options.replace('false', '"false"').replace('true', '"true"'))
    if info:
        options['pulseWidth'] = str(options['pulseWidth'])
        options['pulse width'] = options.pop('pulseWidth')
        options['ota unlock'] = options.pop('otaUnlock')
    elif signal:
        options['signal strength'] = options.pop('signalStrength')
    for key in options:
        i = 0
        string = [key, str(options[key])]
        if len(''.join(string)) != 28:
            i = 28 - len(''.join(string))
        formatted_options.append(string[0] + '.'*i + string[1])
    return formatted_options


def signal(device, signal):
    signal = options_preparation(signal)
    header(device[0])
    print(r'║                                 Signal                                 ║')
    print(r'║                                                                        ║')
    print(r'║                      {}                      ║'.format(signal[0]))
    print(r'║                                                                        ║')
    print(r'╚════════════════════════════════════════════════════════════════════════╝')
    print(r'')

#TODO: Riordinare le def in base alla funzione
