import datetime   	# used to form timestamp 
import argparse   	#used to parse cmdline arguements to this script

#from pwnybrau_library import publish_log, publish_hec, publish_mqtt
from . import publish_log, publish_hec, publish_mqtt

publish_types = ["STDOUT","LOG", "HEC", "MQTT"]

def publish(message:str, args:argparse.Namespace):
    """ factory method that will send metric"""

    outputtype = str(args.output).upper()

    if outputtype == "STDOUT":
        print(message)
    elif outputtype == "LOG":
        publish_log.publish(args.output_config, message)
    elif outputtype == "HEC":
        publish_hec.publish(message)
    elif outputtype == "MQTT":
        publish_mqtt.publish(args.output_config,  message)
    else: # DEFAULT to stdout
        publish_stdout(message)

def publish_stdout(value:str):
        print(value)




    
