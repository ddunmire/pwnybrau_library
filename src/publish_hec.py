import argparse   	#used to parse cmdline arguements to this script
import configparser #parse configuration files (like local/splunk_server.conf)
import requests   	# HTTP request NEED TO DENOTE Install PACKAGES NEEDED
import socket     	# unix socket module

import datetime     # used to form timestamp 
import json   	    

def publish_hec(value: str):
	# craft filename
	raise NotImplementedError

	#Using config file to setup Splunk HTTP transfers
	config = configparser.ConfigParser()
	config.read(os.path.join(sys.path[0], 'local/splunk_server.conf'))
	authHeader={'Authorization': 'Splunk '+config['DEFAULT']['token']}
	url = config['DEFAULT']['url']
	index = config['DEFAULT']['index']

  # Format and send
	jsonDict = {'host': str(socket.gethostname()), 'event': 'metric', 'index': index, 'fields':{'PH':str(value),'_value':str(value),'metric_name':'PH'}}
	r = requests.post(url,headers=authHeader,json=jsonDict,verify=False)