import os
import RPi.GPIO as GPIO
import time
import subprocess

PIR_PIN = 4
SHUTOFF_DELAY = 15 * 60 # (15 min * 60 seconds)

def monitorControlFromPIR():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(PIR_PIN, GPIO.IN)

   last_motion_time = time.time()
   turned_off = False

   while True:
      if GPIO.input(PIR_PIN):
         last_motion_time = time.time()
         if turned_off:
            turned_off = False
            print("Turn on monitor")
            turn_on()
      else:
         if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
            turned_off = True
            print("Turn off monitor")
            turn_off()
      time.sleep(0.1)

def turn_on():
   subprocess.call("sh /home/pi/huffpi/monitor_on.sh", shell=True)

def turn_off():
   subprocess.call("sh /home/pi/huffpi/monitor_off.sh", shell=True)

if __name__ == "__main__":
   monitorControlFromPIR()
   
