# Sonoff_DIY_Mode
Sonoff DIY API and tool rewritten from the original source of [itead](https://github.com/itead/Sonoff_Devices_DIY_Tools).

## Goals
I have rewritten the sonoff API and tools trying to make it easyer and much simple possible.

## Introduction
Sonoff DIY tools is used for Sonoff Basic [R3](https://www.itead.cc/sonoff-basicr3-wifi-diy-smart-switch.html), [RFR3](https://www.itead.cc/sonoff-rfr3.html) and [Mini](https://www.itead.cc/sonoff-mini.html) control via LAN, and not via eWeLink app with their servers, no package will come out of your network!

## Enter in DIY mode

***Activate DIY Mode***

Disconnect the device from the power supply before you operate DIY MODE switch.

If you have power on your sonoff for the frist time, perhaps you have to upgrade the firmware version to 3.3.0 or above, to do it you have necessarily to use eWeLink app

1. Open the bottom lid;
2. Plug-in the jumper on the only pin available.

![DIY Mode Activation](https://github.com/Dave0x21/Sonoff_DIY_Mode/blob/first-release/pictures/photo_2019-12-07_10-41-13.jpg)

***Set up LAN***

Sonoff automatically connects to a specific network, you have to create it, you can easly create an hotspot with your smartphone:

WiFi SSID: `sonoffDiy`

WiFi password: `20170618sn`

***Enter sonoff in DIY mode***

Now, with wifi `sonoffDiy` active, power on your sonoff and watch the blue led blinking:

- Fast double blinking indicates that the device enter the DIY MODE and connect to the WiFi  (SSID: `sonoffDiy` and password: `20170618sn`)  successfully.
- Fast single blinking indicates that the device not connecting to WiFi. please check the WiFi SSID and password was set successfully or not, please check whether your firmware version is 3.3.0 (or above), check the WiFi router or hotspot support mDNS service or not.

***Enjoy the DIY mode***

Now be sure to connect your pc to the same LAN of the sonoff and start the main.py

![Screen1](https://github.com/Dave0x21/Sonoff_DIY_Mode/blob/first-release/pictures/screenshot1.png)

![Screen2](https://github.com/Dave0x21/Sonoff_DIY_Mode/blob/first-release/pictures/screenshot2.png)

![Screen3](https://github.com/Dave0x21/Sonoff_DIY_Mode/blob/first-release/pictures/screenshot3.png)
