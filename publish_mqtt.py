
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
		# init variables
		self.mqttBroker = ""
		self.mqttPort = 1883  				# default to TCP with username and password

		self.use_TLS = False
		self.use_CN_as_username = False
		self.use_insecure_tls = False
		self.caCertsPath = None				#path to folder holding CA Certs (None = use OS default CA's)
		self.certFile = None					#path to client cert. (public)
		self.keyFile = None							#path to client cert key (private)

		self.username = ""
		self.password = ""

		# open configFile
		scp = SafeConfigParser()
		found = scp.read(args.output_config)
		#TODO: check if file exists.

		if (scp.has_section("MQTT") ):
			#TODO: try/catch to capture any missing value & validate them 
			#MQTT endpoint 
			self.mqttBroker = scp["MQTT"]["broker"] 	# "test.mosquitto.org"
			self.mqttPort = int(scp["MQTT"]["port"])	# 1883 

			#MQTT TLS Encryption
			if scp.has_option("MQTT", "use_TLS"): 
				if (scp["MQTT"]["use_TLS"].lower() == "true"):
					self.use_TLS = True 	

				if scp.has_option("MQTT", "use_CN_as_username") and (scp["MQTT"]["use_CN_as_username"].lower() == "true"):
					self.use_CN_as_username = True 	
				if scp.has_option("MQTT", "use_insecure_tls") and (scp["MQTT"]["use_insecure_tls"].lower() == "true"):
					self.use_insecure_tls = True 	

				if (scp.has_option("MQTT", "caCertPath")):
					self.caCertsPath = scp["MQTT"]["caCertPath"] 	
				if (scp.has_option("MQTT", "certfile")):
					self.certFile = scp["MQTT"]["certfile"] 	
				if (scp.has_option("MQTT", "keyfile")):
					self.keyFile = scp["MQTT"]["keyfile"] 		

			#MQTT Auth
			if scp.has_option("MQTT", "username"):
				self.username = scp["MQTT"]["username"] 		# username
			if scp.has_option("MQTT", "password"):
				self.password = scp["MQTT"]["password"] 		# password

			#MQTT session: topic, clientid
			self.mqttTopic = scp["MQTT"]["topicPath"]	+ args.name		#"pwnybrau/sensors/[SensorName]"
			
			if scp.has_option("MQTT","clientID"):			# unique ID to send to broker
				self.clientId = scp["MQTT"]["clientID"] # pwnybrau-pi / thingname
			else:
				self.clientId = platform.node()					#: Use hostname if this is missing
		else:
			errMsg ="Error: configuration file: " + args.output_config + " does not contain MQTT stanza."
			sys.exit(errMsg)

		# init mqtt client    https://github.com/eclipse/paho.mqtt.python#publishing
		self.mqttClient = mqtt.Client(self.clientId)
		# Define Callbacks
		# self.mqttClient.on_publish = publishCallback   #skipping dont need callback at the moment
		# self.mqttClient.on_connect_fail = failedConnectionCallback

		# Set Authentication 
		if (self.use_TLS):
			self.mqttClient.tls_set(ca_certs=self.caCertsPath, certfile=self.certFile, keyfile=self.keyFile)  #note we could add ciphers and other stuff
			self.mqttClient.tls_insecure_set(self.use_insecure_tls)
			
			if (self.use_CN_as_username):
				raise Exception("use_CN_as_username(TRUE) FEATURE is not completed yet.")
			else:
				self.mqttClient.username_pw_set(self.username, self.password)

		else: #not (self.username == "" or self.password == "" ):
			self.mqttClient.username_pw_set(self.username, self.password)

		# Connect
		rtn = self.mqttClient.connect(self.mqttBroker, port=self.mqttPort)

		#TODO:  Need Connection checking here.  Dont start the loop until we have a connection.

		self.mqttClient.loop_start()
		pass

	# Destructor
	def __del__(self) -> None:
		self.mqttClient.loop_stop()
		self.mqttClient.disconnect()

	# Implementations
	def publish(self, message: str):
		if not self.mqttClient.is_connected(): 
			rtn = self.mqttClient.reconnect()

		ret: mqtt.MQTTMessageInfo = self.mqttClient.publish(topic=self.mqttTopic, payload=message)
		# TODO: check publish return value
		pass

#
#def publishCallback(client, userdata, result):
#	print(result)

