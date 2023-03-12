import smtplib
import time
import subprocess
import logging as log
import os
from dotenv import load_dotenv
import random
import re
import socket

GREETING_ARRAY = ["Hi", "Good Morning", "Have a nice day", "Hello", "Hey, how are you?"]

time.sleep(100)
try:
	server = smtplib.SMTP('smtp-mail.outlook.com', 587)
	test = subprocess.check_output("tmux capture-pane -pS Mysession", shell=True)
	t = re.findall(r"\\nForwarding.+tcp:\/\/(.+)-> localhost:22\\n", str(test))[0].strip()
	s = re.findall(r"\\nForwarding.+tcp:\/\/(.+)-> localhost:25565\\n", str(test))[0].strip()
	server.starttls()
	load_dotenv()
	USER = os.getenv('USER')
	server.login(USER, os.getenv('PASSWORD'))
	server.ehlo()
	time.sleep(10)
	sender = USER
	receivers = os.getenv('RECEIVERS').split()
	server.sendmail(sender, receivers, f"Subject: Good morning\n\n" +
	                f"Hello this is the domain for the server {t}\n\nminecraft server:{s}\n\n" +
	                random.choice(GREETING_ARRAY))
	log.basicConfig(filename='/home/moshe/startup/log.txt', level=log.DEBUG, format='%(asctime)s %(message)s')
	log.info('Email sent')
	server.quit()
except Exception as e  :
    print(str(e))
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("127.0.0.1", 6958))
