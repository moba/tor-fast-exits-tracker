#!/usr/bin/env python
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

import shelve
import sys

db = shelve.open('store.db')

all_relays = {} 
all_dates = set() 
for date, relay_groups in db.iteritems():
   all_dates.add(date)
   for group in relay_groups.values():
      for relay in group:
         fingerprint = relay['fingerprint']
         nickname = relay['nickname']
         data = all_relays.get(fingerprint)
         if data is None: 
            dates = set()
         else: 
            (previous_nick,dates) = data
         dates.add(date)
         all_relays[fingerprint]=(nickname,dates)
 
db.close()

for fingerprint,(nickname,dates) in all_relays.items():
   date_counter = 0
   for date in all_dates:
      date_counter += 1
      if date_counter == 1:
         print nickname.ljust(20) + fingerprint + " ", 
      if date in dates:
         sys.stdout.write('.')
      else:
         sys.stdout.write(' ')
   print "" 
