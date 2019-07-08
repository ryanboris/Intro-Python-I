"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def pyCal():
    current_year = datetime.now().year
    current_month = datetime.now().month
    if len(sys.argv) == 1:
        calendar.prmonth(current_year, current_month, w=7, l=5)
    elif len(sys.argv) == 2:
        calendar.prmonth(current_year, int(sys.argv[1]), w=7, l=5)
    elif len(sys.argv) == 3:
        calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]), w=7, l=5)
    else:
        print('Please format your command line execution of the program as: `14_cal.py month(M or MM no 0M!) year(YYYY)`')
    exit()


pyCal()
