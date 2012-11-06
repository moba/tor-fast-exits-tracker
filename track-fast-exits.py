#!/usr/bin/env python
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from compass import compass 
from datetime import datetime
import os
import json
import shelve

def load_data(path):
    return json.load(file(path))

if '__main__' == __name__:
    parser = compass.create_option_parser()
    (options, args) = parser.parse_args()
    options.fast_exits_only = True
    options.top = -1
    fast_exit_options = 1 
    if options.download:
        compass.download_details_file()
        print "Downloaded details.json.  Re-run without --download option."
        exit()
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compass/details.json')):
        parser.error("Did not find details.json.  Re-run with --download.")
    current = load_data(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compass/details.json'))
    date = current['relays_published'].encode('ascii','ignore')
    print date
    stats = compass.RelayStats(options)
    db = shelve.open('store.db')
    db[date] = stats.relays
    db.close() 
