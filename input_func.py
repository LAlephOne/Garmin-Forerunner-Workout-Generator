#!/usr/bin/env python

import datetime
import dateutil

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def confirm(prompt_string="Confirm", 
			allow_empty=False, 
			default=False):
  ordered_prompt = (prompt_string, "Yes", "No") if default else (prompt_string, "No", "Yes")
  if allow_empty:
    formatted_prompt = '%s [%s]|%s: ' % ordered_prompt
  else:
    formatted_prompt = '%s %s|%s: ' % ordered_prompt
 
  while True:
    answer = raw_input(formatted_prompt).lower()
 
    if answer == "" and allow_empty:
      return default
    elif answer in ("y", "ye", "yes", "true", "1"):
      return True
    elif answer in ("n", "no", "false", "0"):
      return False
    else:
      print "Please enter yes or no.\n"

def get_date(): 
	while True:
		try:
			date = raw_input("What is the date of your race? ")
			race_date = dateutil.parser.parse(date)
			pretty_date = custom_strftime("%A, %B {S}, %Y", race_date)
			if confirm(prompt_string="Your race is on {0}?".format(pretty_date), 
						allow_empty=True, 
						default=True):
				break
		except ValueError:
			print "Unable to parse input: {0}\n".format(date)
	return race_date

def get_int(prompt, low=1, high=7):
	return_int = 0
	while not low<=return_int<=high:
		try:
			int_candidate = raw_input(prompt)
			return_int = int(int_candidate)
		except ValueError:
			print "Unable to parse input: {0}".format(int_candidate)
	return return_int
