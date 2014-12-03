#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sensu import Handler
import httplib
import json
import urllib
import base64
import sys


class pingdomHandler(Handler):
	def handle(self):
		self.service_id = self.settings.get('pingdom', {}).get('service_id', '')
		self.api_timeout = self.settings.get('pingdom', {}).get('api_timeout', 15)
		self.api_base = self.settings.get('pingdom', {}).get('api_base', 'api.pingdom.com/api/3.0')
		data = self.event
		client = data.get('client', {}).get('name')
		check = data.get('check', {}).get('name')
		result = data.get('check', {}).get('output')
		status = data.get('check', {}).get('status')
		self.send()


	def send(self):
		params = {
        'source': 'service',
        'data_type': 'nagios',
        'triggerid': self.service_id,
        'data': json.dumps(self.event)
    }
		post_params = urllib.urlencode(params)
		auth = base64.encodestring('anonymous:anonymous').rstrip()
		domain, _, page = self.api_base.partition('/')

		headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "*/*",
               "Authorization": "Basic %s" % auth,
               "User-Agent": "pingdom_es_nagios-1.0"}

		if page:
			url = "/%s/%s" % (page, 'ims.incidents')
		else:
			url = "/%s" % 'ims.incidents'
		conn = httplib.HTTPSConnection(domain, timeout=self.api_timeout)
		conn.request("POST", url, post_params, headers)
		print domain
		print url
		print post_params
		print headers
		resp = conn.getresponse()
		print resp.__dict__
		return resp

if __name__=='__main__':
	p = pingdomHandler()
	sys.exit(0)
