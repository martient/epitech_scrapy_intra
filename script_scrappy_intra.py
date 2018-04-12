#!/usr/bin/env python

# @Author: Arnaud
# @Date:   2018-04-12T21:15:14+02:00
# @Project: Epitech project
# @Filename: script_scrappy_intra.py
# @Last modified by:   Arnaud
# @Last modified time: 2018-04-12T21:16:51+02:00
import json
import urllib
import ConfigParser
import os

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

url = config.get('INTRANET LINK', 'account')
reponse = 0
data = 0

def main():
	print(url)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	i = 0
	while i < 10:
		print(data["board"]["projets"][i]["title"] + " - START:" + data["board"]["projets"][i]["timeline_start"] + " - END:" + data["board"]["projets"][i]["timeline_end"])
		i += 1
		pass
	pass

if url is 'changeme':
	url = url + "?format=json"
	main()
	pass
else:
	print("Error: Scrappy can't acces to the web service intra.epitech.eu, please enter yout Oauth link")
	print()
	print("Go to: https://intra.epitech.eu/admin/autolog")
	pass