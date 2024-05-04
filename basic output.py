import board
import time
import digitalio

led_a = digitalio.DigitalInOut(board.GP2)
led_a.direction = digitalio.Direction.OUTPUT

time.sleep(1)
led_a.value = True
time.sleep(1)
led_a.value = False


