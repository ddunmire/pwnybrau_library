
import datetime     # used to form timestamp
import argparse   	#used to parse cmdline arguements to this script
from configparser import SafeConfigParser #parse configuration files (like local/splunk_server.conf)
import sys
from . publisher import Publisher

class publish_log(Publisher):
	#constructor
	def __init__(self, args:argparse.Namespace) -> None:
		super().__init__()
		#self.__args = args     # debugging only. Probably do not want to keep this.
		
		# open configfile
		scp = SafeConfigParser()
		found = scp.read(args.output_config)
		
		if (scp.has_section("LOG")):
			if (scp.has_option("LOG", "logPrefix")):
				#fileprefix = scp["LOG"]["logPrefix"]
				# craft filename
				today=datetime.date.today()
				self.logfile = scp["LOG"]["logPrefix"] + "." + str(today.year) + "." + str(today.month) + "." + str(today.day) + ".log"

			else:
				sys.exit("Configuration File: "+ args.output_config + " is missing option logPrefix in stanza [LOG]")
		else:
			sys.exit("Configuration File: "+ args.output_config + " is missing stanza [LOG]")


	def publish(self, message: str):
		#write to file
		f = open(self.logfile, "a")
		f.write(message + "\n")
		f.close()
