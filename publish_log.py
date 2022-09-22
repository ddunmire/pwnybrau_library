
import datetime     # used to form timestamp
from configparser import SafeConfigParser #parse configuration files (like local/splunk_server.conf)
import sys

def publish(configFile: str, message: str):
	# open configfile
	scp = SafeConfigParser()
	found = scp.read(configFile)
	
	if (scp.has_section("LOG")):
		if (scp.has_option("LOG", "logPrefix")):
			fileprefix = scp["LOG"]["logPrefix"]
		else:
			sys.exit("Configuration File: "+ configFile + " is missing option logPrefix in stanza [LOG]")
	else:
		sys.exit("Configuration File: "+ configFile + " is missing stanza [LOG]")

	# craft filename
	today=datetime.date.today()
	logfile = fileprefix + "." + str(today.year) + "." + str(today.month) + "." + str(today.day) + ".log"
	#write to file
	f = open(logfile, "a")
	f.write(message + "\n")
	f.close()
