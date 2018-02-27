#!/usr/bin/python
import time
import webbrowser

total_count=3
count=0


while(count<total_count):
	print(" The program started at: "+time.ctime())
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=DqmIT3dVQyY")
	count=count+1
