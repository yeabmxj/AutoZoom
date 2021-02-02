import pyautogui as pyg
import webbrowser as wb
import datetime
import time
import click

def format_date(x):
	date_list = x.split(sep="-")
	return list(map(int, date_list))

def format_time(x):
	time_list = x.split(sep="-")
	return list(map(int, time_list))

def given_datetime(given_date, given_time):
	return datetime.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])

def join_meeting(zoom_link, meeting_date, meeting_time):
	meeting_date_x = format_date(meeting_date)
	meeting_time_x = format_time(meeting_time)
	required_datetime = given_datetime(meeting_date_x, meeting_time_x)

	# time difference
	wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()	
	print("Your ZOOM meeting starts in " + str(wait_time_sec/60) + " min")
	time.sleep(wait_time_sec)

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

