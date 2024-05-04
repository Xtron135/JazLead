import board
import time
import digitalio

sensor0= digitalio.DigitalInOut(board.GP2)
sensor1 = digitalio.DigitalInOut(board.GP3)
sensor2 = digitalio.DigitalInOut(board.GP4)
sensor3 = digitalio.DigitalInOut(board.GP5)
sensor4 = digitalio.DigitalInOut(board.GP6)

sensor0.direction = digitalio.Direction.INPUT
sensor1.direction = digitalio.Direction.INPUT
sensor2.direction = digitalio.Direction.INPUT
sensor3.direction = digitalio.Direction.INPUT
sensor4.direction = digitalio.Direction.INPUT

sensor0.pull = digitalio.Pull.UP
sensor1.pull = digitalio.Pull.UP
sensor2.pull = digitalio.Pull.UP
sensor3.pull = digitalio.Pull.UP
sensor4.pull = digitalio.Pull.UP

while True:
    print("%.1f %.1f %.1f %.1f %.1f" % (sensor0.value, sensor1.value, sensor2.value, sensor3.value, sensor4.value))
    time.sleep(0.1)