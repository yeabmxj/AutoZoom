import pyautogui as pyg
import webbrowser as wb
import datetime
import time
import click

def format_data(x):
	data_list = x.split(sep="-")
	return list(map(int, data_list))

def given_datetime(given_date, given_time):
	return datetime.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])

def wait_time(meeting_date, meeting_time):
	meeting_date_x = format_data(meeting_date)
	meeting_time_x = format_data(meeting_time)
	required_datetime = given_datetime(meeting_date_x, meeting_time_x)

	# time difference
	wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()	
	print("Your ZOOM meeting starts in " + str(wait_time_sec/60) + " min")
	time.sleep(wait_time_sec)

def join_meeting(zoom_link, meeting_date, meeting_time):
	wait_time(meeting_date, meeting_time)

	# zoom stuff
	chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
	wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))
	
	wb.get('chrome').open(zoom_link, new=2)
	time.sleep(5)
	pyg.click(x=2053, y=490, clicks=1, interval=0, button='left') #zoom app option
	time.sleep(10)
	pyg.click(x=2078, y=731, clicks=1, interval=0, button='left') #maximize zoom app
	time.sleep(3)
	pyg.click(x=1897, y=957, clicks=1, interval=0, button='left')

def leave_meeting(meeting_date, meeting_time):
	wait_time(meeting_date, meeting_time)

	pyg.click(x=3739,y=2110, clicks=2, interval=0, button='left')
	time.sleep(2)
	pyg.click(x=3590,y=1955, clicks=1, interval=0, button='left')

#join_meeting("https://us04web.zoom.us/j/77714464098?pwd=a1ZOY1hRenpBU3NWbUlEaXB5SWNjQT09", "02-02-2021", "00-36-00")
leave_meeting()