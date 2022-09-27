from abc import abstractmethod
import argparse
import sys

from pwnybrau_library.publisher import Publisher
from pwnybrau_library.publish_stdout import publish_stdout   	#used to parse cmdline arguements to this script
from pwnybrau_library.publish_log import publish_log   	#used to parse cmdline arguements to this script
from pwnybrau_library.publish_mqtt import publish_mqtt   	#used to parse cmdline arguements to this script
#from pwnybrau_library.publish_hec import publish_stdout   	#used to parse cmdline arguements to this script


#from pwnybrau_library import publish_log, publish_hec, publish_mqtt
#from . import Publisher, publish_log, publish_hec, publish_mqtt

class PublisherFactory(object):
    # possible types of publisher (ie endpoint types)
    # @staticmethod 
    # def PublisherTypes() -> list:
    #     return ["STDOUT","LOG", "HEC", "MQTT"]
    PublisherTypes: list= ["STDOUT","LOG", "HEC", "MQTT"]

    @staticmethod 
    def factory(args:argparse.Namespace) -> Publisher:
        """ factory method that will send metric"""
        outputtype = str(args.output).upper()

        if outputtype == "LOG":
            return publish_log(args)
            
        elif outputtype == "HEC":
            #publish_hec.publish(message)
            sys.exit("HEC publisher not implemented yet.")

        elif outputtype == "MQTT":
            #publish_mqtt.publish(args.output_config)
            return publish_mqtt(args)

        else: # DEFAULT to stdout
            return publish_stdout()       

        return 




# def publish(message:str, args:argparse.Namespace):
#     """ factory method that will send metric"""

#     outputtype = str(args.output).upper()

#     if outputtype == "STDOUT":
#         print(message)
#     elif outputtype == "LOG":
#         publish_log.publish(args.output_config, message)
#     elif outputtype == "HEC":
#         publish_hec.publish(message)
#     elif outputtype == "MQTT":
#         publish_mqtt.publish(args.output_config,  message)
#     else: # DEFAULT to stdout
#         publish_stdout(message)

# def publish_stdout(value:str):
#         print(value)




    
