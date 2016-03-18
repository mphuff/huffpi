import os
import time
import subprocess

def startIceweaselKiosk():
   time.sleep(5)
   subprocess.call("iceweasel -P 'kiosk' --no-remote http://www.micahhuff.com", shell=True)

if __name__ == "__main__":
   startIceweaselKiosk()
