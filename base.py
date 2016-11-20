import RPi.GPIO as GPIO
import time

echo_pin = 20
trigger_pin = 21
speed_of_sound = 34300

def initialize():
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(echo_pin, GPIO.IN)
  GPIO.setup(trigger_pin, GPIO.OUT)

def measure():
  try:
    initialize()
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.000001)
    GPIO.output(trigger_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
      pulse_start = time.time()
    while GPIO.input(echo_pin) == 1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * speed_of_sound / 2.0

    return distance

  except UnboundLocalError:
    GPIO.cleanup()
    return measure()

  finally:
    GPIO.cleanup()

