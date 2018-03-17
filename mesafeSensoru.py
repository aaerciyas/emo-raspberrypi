import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
	pulseStart = time.time() #echo pinine iletilmesi bekleniyor

while GPIO.input(ECHO) == 1:
	pulseEnd = time.time() # echo pinine iletilen zaman

pulseDuration = pulseEnd - pulseStart
distance = pulseDuration * 17150 # ses hizi 343m/s dir. gidis ve donus
#hesaba katildiginda 2ye bolunerek 17150cm/s elde edilir
distance = round(distance,2) #2 ondalik basamak alir

print "Distance", distance,"cm"
GPIO.cleanup()
