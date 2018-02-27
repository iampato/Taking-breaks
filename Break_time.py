#!/usr/bin/python
import time
import webbrowser

count=0
total_count=int(input("Enter number of times you want it to repeat: "))
wait_time=input("Enter the number of hours  to wait befire the break: ")

while(count<total_count):
	print(" The program started at: "+time.ctime())
	time.sleep(wait_time*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=DqmIT3dVQyY")
	count=count+1
