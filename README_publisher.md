# **pwnybrau_library**
This is a library for common functionality that pwnybrau components can use.  Below is a list of the files and their uses.

## **publisherfactory.py**
This class factory for creating publisher objects that allows a metric to be sent to some endpoint.  Example: stdout, log file,  Splunk HEC or MQTT broker-topic

## **publish.conf.template**
This is an example of a publisher.conf file that has all the configuration parameters to connect to a specific end point.   This is done as MQTT, HEC and log file have very different configuration needs.

## **publish_stdout.py**
This is the default publisher.  It simply writes to standard out.

## **publish_mqtt.py**
MQTT client that will handle publishing messaged to a MQTT topic.  Configured via the [MQTT] stanza in the publish.conf

## **publish_log.py**
Writes to a LOG file.  Configured via the [LOG] stanza in the publish.conf

## **publish_hec.py** : TBD
Splunk HEC client for publishing to a splunk indexers.  Configured vai the [HEC] stanza in the publish.conf


