import datetime     # used to form timestamp
from configparser import SafeConfigParser #parse configuration files (like local/splunk_server.conf)
import sys
import argparse   	#used to parse cmdline arguements to this script
from . publisher import Publisher

class publish_stdout(Publisher):  
    #constructor
    def __init__(self) -> None:
        super().__init__()

    def publish(self,message:str=""):
        print(message)