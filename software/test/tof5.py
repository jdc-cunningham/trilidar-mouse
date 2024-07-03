import time

import RPi.GPIO as GPIO

toft_shutdown = 17
tofl_shutdown = 27
tofr_shutdown = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(toft_shutdown, GPIO.OUT)
GPIO.setup(tofl_shutdown, GPIO.OUT)
GPIO.setup(tofr_shutdown, GPIO.OUT)

GPIO.output(toft_shutdown, GPIO.LOW)
GPIO.output(tofl_shutdown, GPIO.LOW)
GPIO.output(tofr_shutdown, GPIO.LOW)

# GPIO.output(toft_shutdown, GPIO.HIGH)
# GPIO.output(tofl_shutdown, GPIO.HIGH)
GPIO.output(tofr_shutdown, GPIO.HIGH)

while True:
  print('keep down')
  time.sleep(1)