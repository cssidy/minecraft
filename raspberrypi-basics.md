# Raspberry Pi 3 Basics

The Raspberry Pi 3 is the third generation Raspberry Pi. It replaced the Raspberry Pi 2 Model B in February 2016. Compared to the Raspberry Pi 2 it has:

* A 1.2GHz 64-bit quad-core ARMv8 CPU
* 802.11n Wireless LAN
* Bluetooth 4.1
* Bluetooth Low Energy (BLE)

Like the Pi 2, it also has:

* 1GB RAM
* 4 USB ports
* 40 GPIO pins
* Full HDMI port
* Ethernet port
* Combined 3.5mm audio jack and composite video
* Camera interface (CSI)
* Display interface (DSI)
* Micro SD card slot (now push-pull rather than push-push)
* VideoCore IV 3D graphics core

# Raspbian

Raspbian is the Foundation’s official supported operating system. Raspbian comes pre-installed with plenty of software for education, programming and general use. It has Python, Scratch, Sonic Pi, Java, Mathematica and more.

You can purchase a micro SD card (NOOBS) with Raspbian pre-installed, or create your own.

![Raspbian desktop](http://robertan.com/home/wp-content/uploads/2016/04/raspbian.png "Raspbian desktop")

Download the image file from the [Raspbian website](https://www.raspberrypi.org/downloads/raspbian/), then extract it from the torrent/zip folder it came in.

Insert the blank 8GB micro SD card into the SD card adapter and insert the conjoined pair into the desktop's SD card slot reader.

With the Make Startup Disk utility, which comes preinstalled in the Ubuntu GUI, choose the Raspbian .img file (2016-09-23-raspbian-jessie.img) from your folders and select the appropriate SD 
card destination. Click the start button, then wait a couple minutes for the SD card to finish formatting. 

Alternatively, you can create a bootable SD card in the Linux command line, where 'user' is your user account, and '/dev/sdb' is the path to your SD card. I am not sure how this differs from Windows or Mac environments, so you should research the correct syntax if that's what you are using.

```
sudo dd bs=4M if=/home/user/Downloads/2016-09-23-raspbian-jessie.img of=/dev/sdb
```

Remove the SD card from the desktop computer and remove the micro SD card from the adapter. Insert the micro SD card into the Raspberry Pi 3. If you boot up your Pi, the OS should install.

# Ubuntu MATE

To install Ubuntu MATE, follow the directions above for Raspbian, but instead load a MATE image file onto the micro SD card.

![Ubuntu Mate desktop](https://ubuntu-mate.org/gallery/Screenshots/04_DESKTOP.png "Ubuntu Mate desktop")

## Resize File System

After setting up Ubuntu MATE for the first time on your Raspberry Pi, the file system will be restricted to the size of the origin
image, which is about 3.9 GB. You can resize the file system by navigating to System > Welcome > Raspberry Pi Information.

## Incompatible Software

Some packages available for Ubuntu have only been written and compiled for the i386 or amd64 architecture. 
As the Raspberry Pi is based on armv7, these packages will not be available to install. Depending on the package, it may be
possible to compile these yourself or use and existing port (Ubuntu Mate, 2016).

### Incombatible:

* Google Chrome
* Minecraft (Java Edition)
* Adobe Flash
* VirtualBox

### Combatible:

* Chromium
* Minecraft: Pi Edition
* Pepper Flash
* QEMU

## Upgrades & Updates

**Do not attempt** to upgrade you Raspberry Pi to a newer version of the distribution (for instance, from 15.04 to 15.10), as the underlying
kernel is not designed to do this. This process will not only take a long time to complete, but will potentially fill up your SD card
until there is no more free space, prevent installation from booting, corrupt the SD card, or cause severe glitches. Instead, backup
all of your data and re-flash the card with the new image if you want to upgrade distributions.

You can install regular updates via the Software Updater.

If you want to update the kernel, you can issue the terminal command:

```
sudo rpi-update
```

## Hardware Acceleration

Unlike in Raspbian, Ubuntu MATE does not support hardware accelerated applications. Applications that depend on OpenGL ES libraries
or require the GPU will fail to start. If you want to play videos, the pre-installed application omxplayer should do the job.
But if you are trying to play MPEG-2 or VC-1 video files you'll want to install their license keys from the Raspberry Pi Store.

## Drivers

While a wide range of hardware is compatible with Ubunutu MATE, there are some components and peripherals
that require proprietary drivers to function properly. Installing the firmware package is often required to get some
devices, typically Bluetooth and Wi-Fi, to work correctly.
