import board
import time
import digitalio

button_a = digitalio.DigitalInOut(board.GP20)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

while True:
    print(button_a.value)
    time.sleep(0.1)