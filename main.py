import lib
import RPi.GPIO as GPIO

try:
    lib.main()

except KeyboardInterrupt:
    print("Program interrupted.")

except Exception as e:
    print("Something went wrong.")
    print(e)

finally:
    GPIO.cleanup()
