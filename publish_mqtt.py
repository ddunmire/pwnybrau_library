
import argparse   	#used to parse cmdline arguements to this script
import datetime     # used to form timestamp 
import sys
import platform

from configparser import SafeConfigParser #parse configuration files (like local/splunk_server.conf)
import paho.mqtt.client as mqtt

def publish(configFile: str, message: str=""):
	# open configFile
	#TODO: check if file exists.
	#TODO: add credentials

	scp = SafeConfigParser()
	found = scp.read(configFile)
	
	if (scp.has_section("MQTT") ):
		mqttBroker = scp["MQTT"]["broker"] 	#"test.mosquitto.org"
		mqttPort = int(scp["MQTT"]["port"])	#1883 
		mqttTopic = scp["MQTT"]["topic"]	#"pwnybrau"
		if scp.has_option("MQTT","clientID"):
			clientId = scp["MQTT"]["clientID"] 	#"yourMom"	
		else:
			clientId = platform.node()

	else:
		errMsg ="Error: configuration file: " + configFile + " does not contain MQTT stanza."
		sys.exit(errMsg)

									#https://test.mosquitto.org/
	

	# init mqtt client
	mqttClient = mqtt.Client(clientId)
	mqttClient.connect(mqttBroker, mqttPort)
	mqttClient.publish(topic=mqttTopic, payload=message)

	#





	# craft filename
	#raise NotImplementedError
