import RPi.GPIO as GPIO
import time

led1 = 11
led2 = 13

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

def flipflop():
	GPIO.output(led1,GPIO.HIGH)
	GPIO.output(led2,GPIO.LOW)
	time.sleep(1)
	GPIO.output(led1,GPIO.LOW)
	GPIO.output(led2,GPIO.HIGH)
	time.sleep(1)

while True:
	flipflop()

