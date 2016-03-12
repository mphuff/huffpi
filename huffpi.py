import os
from time import *

sleep(5)
os.system("iceweasel -P 'kiosk' --no-remote http://www.micahhuff.com")
sleep(5)
os.system('xdotool key --clearmodifiers F11')
