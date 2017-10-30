#!/usr/bin/env python

from datetime import datetime

x=0

def validate(date_text):
    try:
        datetime.strptime(date_text, "%a %b %d %H:%M:%S")
        return True
    except ValueError:
        return False

while (x<1):

   date = raw_input("Please enter a valid date:")
   print "You entered:", date


   if validate (date):
      print date," Is a valid date"
      x = x + 1
   else:
      print date," Is invalid please enter a valid date"



