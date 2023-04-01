import smtplib
import time
import logging as log
import os
from dotenv import load_dotenv
import random
import socket
import requests

GREETING_ARRAY = ["Hi", "Good Morning", "Have a nice day", "Hello", "Hey, how are you?"]

time.sleep(100)
try:
	server = smtplib.SMTP('smtp-mail.outlook.com', 587)
	serverDomain = ''
	minecraftServerDomain = ''
	stableServerDomain = ''
	for site in requests.get("http://localhost:4040/api/tunnels/").json()['tunnels']:
		if 'first' in site['uri']:
			serverDomain = site['public_url']
		elif 'third' in site['uri']:
			minecraftServerDomain = site['public_url']
		elif 'second' in site['uri']:
			stableServerDomain = site['public_url']

	server.starttls()
	load_dotenv()
	USER = os.getenv('USER')
	server.login(USER, os.getenv('PASSWORD'))
	server.ehlo()
	time.sleep(10)
	sender = USER
	receivers = os.getenv('RECEIVERS').split()
	server.sendmail(sender, receivers, f"Subject: Good morning\n\n" +
	                f"Hello this is the domain for the server {serverDomain}\n\nminecraft server:{minecraftServerDomain}" +
					f"\n\nstable diffusion domain: {stableServerDomain}\n\n" +
	                random.choice(GREETING_ARRAY))
	log.basicConfig(filename='/home/moshe/startup/log.txt', level=log.DEBUG, format='%(asctime)s %(message)s')
	log.info('Email sent')
	server.quit()
except Exception as e  :
	print(str(e))
	socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("127.0.0.1", 6958))
