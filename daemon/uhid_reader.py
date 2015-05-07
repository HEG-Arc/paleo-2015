# -*- coding: UTF-8 -*-
# uhid_reader.py
#
# Copyright (C) 2015 HES-SO//HEG Arc
#
# Author(s): Cédric Gaspoz <cedric.gaspoz@he-arc.ch>
#
# This file is part of Gestion'air 2015.
#
# Gestion'air 2015 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gestion'air 2015 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gestion'air 2015. If not, see <http://www.gnu.org/licenses/>.
#
# To kick off the script, run the following from the python directory:
#   python uhid_reader.py start|stop|restart (must be run as root!)

# Stdlib imports
import logging
import time
import sys

# Third-party libs imports
import daemonocle
from evdev import InputDevice, ecodes, list_devices, categorize

# Gestion'air imports
from uhid_manager import send_code

KEYCODES = {
    19: u'R', 21: u'Y', 34: u'G', 48: u'B'
}

READER_DEVICE = "Universal Human Interface Device Universal Human Interface Device"


def reader_shutdown(message, code):
    logging.warning('U-HID Reader is stopping')
    logging.debug(message)


def get_device():
    dev = None
    # TODO: find a way to detect the right device
    #devices = map(InputDevice, list_devices())
    #for device in devices:
    #    if device.name == READER_DEVICE:
            #dev = InputDevice(device.fn)
    dev = InputDevice('/dev/input/event20')
    return dev


def main():
    logging.basicConfig(
        filename='/var/log/gestionair/uhid_reader.log',
        level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
    )
    logging.warning('U-HID Reader daemon is starting')
    while True:
        logging.info("Getting the device...")
        dev = get_device()

        if dev:
            logging.info("We got the device...")
            dev.grab()
            while True:
                try:
                    for event in dev.read_loop():
                        if event.type == ecodes.EV_KEY:
                            data = categorize(event)
                            logging.debug("Scancode: CODE %s | KEYSTATE %s" % (data.scancode, data.keystate))
                            if data.keystate == 1:  # Down events only
                                button = u'{}'.format(KEYCODES.get(data.scancode))
                                if button != 'None':
                                    logging.info("Valid code: %s" % button)
                                    msg = send_code(button)
                                    logging.info("Response: %s" % msg)
                                else:
                                    # The code is invalid, sorry
                                    logging.warning("Wrong scancode: %s" % data.scancode)
                except IOError:
                    logging.error("IOError")
                    break
        time.sleep(2)


if __name__ == '__main__':
    daemon = daemonocle.Daemon(
        worker=main,
        shutdown_callback=reader_shutdown,
        pidfile='/var/run/gestionair/uhid_reader.pid',
    )
    daemon.do_action(sys.argv[1])