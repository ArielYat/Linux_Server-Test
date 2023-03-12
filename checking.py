import os
import time
import subprocess
try:
    test = subprocess.check_output("tmux capture-pane -pS MySession", shell=True)
    t = str(test)
    print(t)
    if (not ("online" in t)):
        os.system("tmux kill-session -t MySession")
        os.system("/home/moshe/startup/startupNgrok && /usr/bin/python3 /home/moshe/startup/email123.py")

except:
    os.system("tmux kill-session -t MySession")
    os.system("/home/moshe/startup/startupNgrok && /usr/bin/python3 /home/moshe/startup/email123.py")
