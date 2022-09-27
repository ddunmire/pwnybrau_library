
import argparse   	#used to parse cmdline arguements to this script
from configparser import SafeConfigParser #parse configuration files (like local/splunk_server.conf)
import sys
import platform
import paho.mqtt.client as mqtt
from . publisher import Publisher

class publish_mqtt(Publisher):

	#constructor
	def __init__(self, args:argparse.Namespace) -> None:
		super().__init__()
		
		# open configFile
		#TODO: check if file exists.
		#TODO: add credentials

		scp = SafeConfigParser()
		found = scp.read(args.output_config)

		if (scp.has_section("MQTT") ):
			#TODO: try/catch to capture any missing value & validate them 
			self.mqttBroker = scp["MQTT"]["broker"] 		#"test.mosquitto.org"
			self.mqttPort = int(scp["MQTT"]["port"])		#1883 
			self.mqttTopic = scp["MQTT"]["topic"]			#"pwnybrau"
			if scp.has_option("MQTT","clientID"):			# unique ID to send to broker
				self.clientId = scp["MQTT"]["clientID"] 	# 
			else:
				self.clientId = platform.node()			#: Use hostname if this is missing
		else:
			errMsg ="Error: configuration file: " + args.output_config + " does not contain MQTT stanza."
			sys.exit(errMsg)

		# init mqtt client    https://github.com/eclipse/paho.mqtt.python#publishing
		self.mqttClient = mqtt.Client(self.clientId)
		# mqttClient.on_publish = publishCallback   #skipping dont need callback at the moment
		rtn = self.mqttClient.connect(self.mqttBroker, port=self.mqttPort)
		self.mqttClient.loop_start()
		pass

	# Destructor
	def __del__(self) -> None:
		self.mqttClient.loop_stop()
		self.mqttClient.disconnect()

	def publish(self, message: str):
		if not self.mqttClient.is_connected(): 
			rtn = self.mqttClient.reconnect()

		ret: mqtt.MQTTMessageInfo = self.mqttClient.publish(topic=self.mqttTopic, payload=message)
		
		# TODO: check publish return value
		pass

#
#def publishCallback(client, userdata, result):
#	print(result)

