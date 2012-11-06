#!/usr/bin/env python
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import shelve

db = shelve.open('store.db')

all_relays = {} 
for date, relay_groups in db.iteritems():
   for group in relay_groups.values():
      for relay in group:
         fingerprint = relay['fingerprint']
         dates = all_relays.get(fingerprint)
         if dates is None: 
            dates = set()
         dates.add(date)
         all_relays[fingerprint]=dates
 
db.close()

for fingerprint,dates in all_relays.items():
   print fingerprint,dates 
