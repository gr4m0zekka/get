import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)
sleep(3)
GPIO.output(17, 0)
sleep(3)
GPIO.output(17, 1)
sleep(3)
GPIO.output(17, 0)
sleep(3)
GPIO.output(17, 1)
sleep(3)
GPIO.output(17, 0)
sleep(3)
GPIO.output(17, 1)
sleep(3)
GPIO.output(17, 0)
sleep(3)
