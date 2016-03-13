import os
from time import *

def startIceweaselKiosk():
   sleep(5)
   os.system("iceweasel -P 'kiosk' --no-remote http://www.micahhuff.com")

if __name__ == "__main__":
   startIceweaselKiosk()
