from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)


def blink():
    led.toggle()
    sleep(1)


while True:
    blink()

