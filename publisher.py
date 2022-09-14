import datetime   	# used to form timestamp 
import argparse   	#used to parse cmdline arguements to this script

import publish_log
import publish_hec
import publish_mqtt
from pwnybrau_library.src.publish_mqtt import publish_mqtt

def publish(args:argparse.Namespace, value:str):
    """ factory method that will send metric"""

    outputtype = str(args.output).upper()

    if outputtype == "STDOUT":
        print(value)
    elif outputtype == "LOG":
        publish_log(args.logfile, value)
    elif outputtype == "HEC":
        publish_hec(value)
    elif outputtype == "MQTT":
        publish_mqtt(value)
    else: # DEFAULT to stdout
        publish_stdout(value)

def publish_stdout(value:str):
        print(value)




    
