import RPi.GPIO as GPIO
import time

leds = [29,31,32,33,35,36,37,38]

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

for i in range(8):
	GPIO.setup(leds[i], GPIO.OUT)
	GPIO.output(leds[i], GPIO.LOW)
while True:
	for i in range(8):
		GPIO.output(leds[i], GPIO.HIGH)
		time.sleep(0.05)
		GPIO.output(leds[i], GPIO.LOW)
	for j in range (7,-1,-1):
		GPIO.output(leds[j], GPIO.HIGH)
		time.sleep(0.05)
		GPIO.output(leds[j], GPIO.LOW)
