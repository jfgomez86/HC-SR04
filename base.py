import RPi.GPIO as GPIO
import time

echo_pin = 21
trigger_pin = 20
speed_of_sound = 34300

def initialize():
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(echo_pin, GPIO.IN)
  GPIO.setup(trigger_pin, GPIO.OUT)

def measure():
  try:
    print "Press Control-C to stop"
    initialize()
    while True:
      GPIO.output(trigger_pin, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(trigger_pin, GPIO.LOW)

      while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
      while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

      pulse_duration = pulse_end - pulse_start
      distance = pulse_duration * speed_of_sound / 2.0

      print("Distance:", distance, "cm")
      time.sleep(0.5)
  except KeyboardInterrupt:
    print "\rStopping"
    return
  finally:
    GPIO.cleanup()

