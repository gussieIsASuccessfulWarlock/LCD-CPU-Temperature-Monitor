#!/usr/bin/python3
from signal import signal, SIGINT ,SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from datetime import datetime
import time
import RPi.GPIO as GPIO
import itertools
import sys
import threading
lcd = LCD()
on = True
done = False
def safe_exit(signum, frame):
	on = False
	time.sleep(00.05)
	sys.stdout.flush()
	sys.stdout.write('\rProgram Ended                 ')
	print(chr(27)+'[2j')
	print(" ")
	print(" ")
	time.sleep(00.35)
	LCD().clear
	time.sleep(00.05)
	LCD().text(" ", 1)
	time.sleep(00.05)
	LCD().text(" ", 1)
	LCD().text(" ", 2)
	tFile.close()
	GPIO.cleanup
	time.sleep(00.05)
	exit(1)

signal(SIGTERM, safe_exit)

signal(SIGHUP, safe_exit)

signal(SIGINT, safe_exit)

def animate():
	loadDots = 0
	loadTime = 30
	for c in itertools.cycle(['|', '/', '-','\\']):
		if done:
			LCD().text(" ", 2)
			break
		sys.stdout.write('\rLoading ' + c)
		sys.stdout.flush()
		if loadTime == 30:
			if loadDots == 0:
				LCD().text("C", 2)
			if loadDots == 1:
				LCD().text("CP", 2)
			if loadDots == 2:
				LCD().text("CPU", 2)
			if loadDots == 3:
				LCD().text("CPUT", 2)
			loadDots = loadDots + 1
			loadTime = 0
		loadTime = loadTime + 1
		time.sleep(0.1)
	sys.stdout.write('\rStarted Central Prossing Unit Theromoter or CPUT!     ')
try:
	on = True
	LCD().text("CPUT", 1)
	print(" ")
	t = threading.Thread(target=animate)
	t.start()
	time.sleep(11)
	done = True
	time.sleep(1)
	print(" ")
	print(" ")
	print(" ")
	print(" ")
        print("  011111010      011111000      01     10      1000000000")
        print(" 11              01     111     10     11          00")
        print("01               11     111     10     11          01")
        print("10               000101101      10     11          11")
        print(" 11              11             100   011          01")
        print("  01010000   11  00        01    1111101   10      11    01")
        print("")
	time.sleep(1)
	print(" ")
	print(" ")
	corf = input("Press C for Celsius or F for Farenheit: ")
	print("Press CTRL and C To Exit")
	print("Press ENTER To Save Reading")
	print(" ")
	count = 0
	while on:
		sys.stdout.flush()
		time.sleep(0.3)
		tFile = open('/sys/class/thermal/thermal_zone0/temp')
		temp = float(tFile.read())
		tempC = temp / 1000
		today = str(round(tempC, 2))
		if corf == 'f' or corf == 'F':
			newToday = (tempC * 9/5) + 32
			sys.stdout.write('\r' + str(round(newToday, 2))  + "°F ")
			lcd.text("Time: " + str(datetime.now().strftime("%H:%M:%S")), 2)
			lcd.text("CPU: " + str(round(newToday, 2)) + " F.", 1)
		else:
			sys.stdout.write('\r' + today  + "°C ")
			lcd.text("Time: " + str(datetime.now().strftime("%H:%M:%S")), 2)
			lcd.text("CPU: " + str(today) + " C.", 1)
except KeyboardInterrupt:
	pass
