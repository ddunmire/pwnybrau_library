import datetime   	# used to form timestamp 
import argparse   	#used to parse cmdline arguements to this script

#from pwnybrau_library import publish_log, publish_hec, publish_mqtt
from . import publish_log, publish_hec, publish_mqtt

def publish(value:str, args:argparse.Namespace):
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




    
