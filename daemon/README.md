# Gestion'air daemon

This daemon is listening for inputs from the U-HID controller and pass them to the web server.

## Installation

To use the daemon with upstart (Ubuntu), you need to copy the uhid_reader.conf file to `/etc/init`

The user must be root in order to have access to evdev. Otherwise you will not be able to listen to the
U-HID device.

Adjust the path of the `uhid_reader.py` file.

Start the service with: `sudo start uhid_reader`
