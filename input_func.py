#!/usr/bin/env python

import datetime
from dateutil.parser import parse
import distance_parse

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

def get_race_date(): 
	while True:
		try:
			date = raw_input("What is the date of your race? ")
			race_date = parse(date)
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

def get_race_distance():
	prompt = "What is the distance of your race (5 k, 1 marathon, etc.)? "

	while True:
		try:
			distance = raw_input(prompt)
			try: input_unit = distance.split()[-1]
			except IndexError: input_unit = None

			while input_unit not in distance_parse.Distance.UNITS:
				print "Unable to parse unit {0}\n".format(input_unit)
				
				distance = raw_input(prompt)
				try: input_unit = distance.split()[-1]
				except IndexError: input_unit = None

			race_dist = distance_parse.Distance(distance)
			if confirm(prompt_string="Your race distance is {0}?".format(distance), 
						allow_empty=True, 
						default=True):
				break
		except ValueError:
			print "Unable to parse input: {0}\n".format(distance)
	return race_dist
