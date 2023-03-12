import os
import time
import subprocess
try:
    test = subprocess.check_output("sudo -u moshe tmux capture-pane -pS MySession", shell=True)
    t = str(test)
    print(t)
    if (not ("online" in t)):
        os.system("/etc/init.d/logmein-hamachi restart")
        time.sleep(10)
        os.system("/usr/bin/hamachi logon")
except:
    os.system("/etc/init.d/logmein-hamachi restart")
    time.sleep(10)
    os.system("/usr/bin/hamachi logon")
