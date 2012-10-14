#Running Plan Generator
##Introduction
This project is mostly an exercise to improve my comfort with the python language.
Secondarially, it's designed to prompt the user for a race date and distance, as
well as for how many days per week they can dedicate to training for their race,
then generate a customized running plan that's ready to be synced to their Garmin
Forerunner GPS watch.

##Usage
You should be able to simply run the program from the terminal, follow the prompts,
and end up with a custom.wkt file exported to the current working directory.

##Requirements
The non-standard-library python module [dateutil](http://labix.org/python-dateutil) is required:
    pip install dateutil

##License
This code has been granted coverage under [MPL2.0](https://www.mozilla.org/MPL/2.0/index.txt)
