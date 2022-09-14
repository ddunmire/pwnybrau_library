
import argparse   	#used to parse cmdline arguements to this script
import datetime     # used to form timestamp 
import json   	    

import argparse   	#used to parse cmdline arguements to this script
import configparser #parse configuration files (like local/splunk_server.conf)

import publisher


def publish_log(logfilename:str, value: str):
	# craft filename
	today=datetime.date.today()
	logfile = logfilename + "." + str(today.year) + "." + str(today.month) + "." + str(today.day) + ".log"
	#write to file
	f = open(logfile, "a")
	f.write(value + "\n")
	f.close()
