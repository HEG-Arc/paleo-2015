# -*- coding: UTF-8 -*-
# uhid_manager.py
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

"""
This manager is used by the UHID_reader in order to send commands to the main application. In our setup where the
reader is not running on the same computer as the main application, the manager uses REST services to transmit
commands from the buttons.
"""

# Stdlib imports
from urllib2 import Request, urlopen, URLError

# Third-party libs imports

# Gestion'air imports


GESTIONAIR_REST_API = "http://localhost:8080/api/command/"
API_COMMAND = {'B': 'start_demo', 'G': 'start_simulator', 'R': 'stop_simulator', 'Y': 'start_fiesta'}


def send_code(code):
    if code in API_COMMAND:
        req = Request(GESTIONAIR_REST_API + API_COMMAND[code] + '/')
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                return "We failed to reach a server (%s)." % e.reason
            elif hasattr(e, 'code'):
                return "The server couldn't fulfill the request (%s)." % e.code
        else:
            return response.read()
    else:
        return "Not a valid code: %s" % code
