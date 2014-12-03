# sensu-pingdom
A sensu handler for sending alerts to pingdom

# dependencies
 * [sensu-py](https://github.com/ehazlett/sensu-py)

# About
This handler uses the pingdom api 3.0 which is not yet public. It is based on the work pubished by pigdom to send alerts from nagios.

# Files
 * pingdom.py: The actual handler that needs to be copied onto the sensu server host
 * pingdome.json: The config file
 * event.json: Sample sensu event for testing purposes

# INSTALL
 * copy the python script into /etc/sensu/handlers/ on the sensu server
 * copy the pingdom.json into /etc/sensu/conf.d/
 * configure the handler as described on the sensu docs
 * follow that guide for setting up pingdom https://www.pingdom.com/guides/#nagios

# testing
 * run the command
 ```
 # api.json has the api config, for the handler to query it about stashes and whatnot
 export SENSU_CONFIG_FILES=./pingdom.json:./api.json
 cat event.json| pingdom.py

