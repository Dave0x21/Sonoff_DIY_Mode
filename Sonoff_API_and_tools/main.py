#################################
#                               #
#       Author: Dave0x21        #
#       Sonoff Config Tool      #
#                               #
#################################

import pickle
import platform
import subprocess
import sys
import time

import mDNS
import menu
import Sonoff_DIY_API as sonoff

SAVED_DEVICES = {}

def clean_terminal():
    CURRENT_OS = platform.system()

    if CURRENT_OS == 'Linux':
        subprocess.call(['tput', 'reset'])
    elif CURRENT_OS == 'Windows':
        subprocess.call('cls', shell=True)
    elif CURRENT_OS == 'Darwin':
        pass


def main_selection(device):
    global SAVED_DEVICES
    menu.main(device)
    try:
        choice = int(input('Choose what to do... '))
    except ValueError:
        # The choice isn't a number so it isn't a valid choise
        print('Choise not valid')
        time.sleep(1)
        return
    if choice == 0: 
        # Stop Execution
        sys.exit()
    elif choice == 1:
        # Get Info 
        info = eval(sonoff.get_Info(device).replace('false', '"false"').replace('true', '"true"'))
        signal = eval(sonoff.get_Signal_Strenght(device).replace('false', '"false"').replace('true', '"true"'))
        clean_terminal()
        menu.info(device, info, signal)
        input('Press any key to continue... ')
    elif choice == 2:
        # Set the state of switch to on
        sonoff.set_ON(device)
    elif choice == 3:
        # Set the state of switch to off
        sonoff.set_OFF(device)
    elif choice == 4:
        # Change the state on power on of the sonoff
        clean_terminal()
        menu.power_on_state(device)
        choise = int(input('Choose from the menù...'))
        evalutate_choise(device, choise)
        print('Done\t🗸')
        time.sleep(1)
    elif choice == 5:
        # Set the Pulse function
        clean_terminal()
        pulse_selection(device)
    elif choice == 6:
        # Change the wifi connection of the sonoff
        change_wifi(device)
    elif choice == 7:
        # Unlock firmware OTA
        sonoff.Unlock_OTA(device)
    elif choice == 8:
        # Flash new firmware
        flash_firmware(device)
    elif choice == 9:
        # Add device
        SAVED_DEVICES[device[0]] = input('Type new name for the sonoff... ')
        pickle.dump(SAVED_DEVICES, open("devices.p", "wb"))
    else:
        # The choice is not valid
        print('Choice not valid...')
        time.sleep(1)


def evalutate_choise(device, choise):
    if choise == 1:
            sonoff.set_Power_On_State(device, 'on')
    elif choise == 2:
        sonoff.set_Power_On_State(device, 'off')
    elif choise == 3:
        sonoff.set_Power_On_State(device, 'stay')
    elif choise == 0:
        pass
    else:
        print('Choise not valid...')
        input('Press any key to continue...')


def power_on_state_selection(device):
    menu.power_on_state(device)
    choice = int(input('Choose what to do... '))
    if choice == 1:
        sonoff.set_Power_On_State(device, 'on')
    elif choice == 2:
        sonoff.set_Power_On_State(device, 'off')
    elif choice == 3:
        sonoff.set_Power_On_State(device, 'stay')
    elif choice == 0:
        pass
    else:
        print('Unknow option selected...')


def pulse_selection(device):
    menu.pulse(device)
    try:
        choice = int(input('Choose what to do... '))
    except ValueError:
        # The choice isn't a number so it isn't a valid choise
        print('Choise not valid')
        time.sleep(1)
        return
    if choice == 1:
        try:
            width = int(input('Insert a value for the pulse width (in seconds, in range of 0.5~36000)... '))
        except ValueError:
            # The choice isn't a number so it isn't a valid choise
            print('Value not valid')
            time.sleep(1)
            return
        # Convert from seconds to milliseconds
        width = width * 1000
        if 500 > width or width > 36000000:
            # If not in range 500~36000000 the value is not valid
            print('The value of the pulse width must be in range of 500~36000000')
        else:
            # Value is good
            sonoff.set_Pulse(device, 'on', width=width)
    elif choice == 2:
        sonoff.set_Pulse(device, 'off')
    elif choice == 0:
        pass
    else:
        print('Unknow selection...')


def device_selection(device):
    while True:
        menu.device(device)
        choice = input('Choose the device... ')
        if choice == '0':
            sys.exit()
        else:
            try:
                return device[int(choice)-1]
            except IndexError:
                print('Unknow device selected')
                time.sleep(1)
                clean_terminal()


def change_wifi(device):
    ssid = input('Insert the SSID... ')
    password = input('Insert the wifi password... ')
    sonoff.set_WiFi(device, ssid, password)


def flash_firmware(device):
    url = input('Insert the url of new firmware... ')
    checksum = input('Insert the checksum of the new firmware... ')
    sonoff.Flash_OTA(device, url, checksum)


def load_device_name(device):
    global SAVED_DEVICES
    try:
        SAVED_DEVICES = pickle.load(open("devices.p", "rb"))
    except FileNotFoundError:
        pass
    for elem in device:
        if elem[0] in SAVED_DEVICES:
            elem.append(SAVED_DEVICES[elem[0]])
        

def main():
    clean_terminal()
    print('Scanning device...')
    device = mDNS.get_device()
    load_device_name(device)
    print('Done\t🗸')
    time.sleep(1)
    clean_terminal()
    if len(device) > 1:
        # If more than one device is online, select one from the list
        device = device_selection(device)
    else:
        device = device[0]
    while True:
        # After all action return always on main meu until exit is selected
        clean_terminal()
        main_selection(device)


if __name__ == '__main__':
    main() 
