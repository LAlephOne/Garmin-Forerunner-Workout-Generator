#!/usr/bin/env python

import xml.etree.ElementTree as ET
import input_func

def main():
	race_date = input_func.get_race_date()
	days_per_week = input_func.get_int(prompt = "How many days per week can you train (1 - 7)? ",
							low = 1, high = 7)
	distance = input_func.get_int(prompt = "How many meters is your race? (5000 - 42195) ",
						low = 5000, high = 42195)

	generate_xml(race_date = race_date,
				 days_per_week = days_per_week,
				 distance = distance)

def generate_xml(race_date = datetime.date.today() + datetime.timedelta(days=7*30),
				 days_per_week = 3,
				 distance = 42195):
	root = ET.Element("TrainingCenterDatabase", 
		{"xmlns":"http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v1", 
		"xmlns:xsi":"http://www.w3.org/2001/XMLSchema-instance",
		"xsi:schemaLocation":"http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v1 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev1.xsd"})
	workouts = ET.SubElement(root, "Workouts")
	running = ET.SubElement(workouts, "Running", {"Name":"Running"})
	folder = ET.SubElement(running, "Folder", {"Name":"Generated {0}".format(datetime.datetime.today())})
	workout = ET.SubElement(folder)

	
if __name__ == '__main__':
	main()
