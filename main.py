import lib
import RPi.GPIO as GPIO

try:
    lib.main()

except KeyboardInterrupt:
    print()

finally:
    GPIO.cleanup()
