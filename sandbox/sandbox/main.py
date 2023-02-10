#!/usr/bin/env python3

from ev3dev2.sensor import Sensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor


left = Sensor(INPUT_2)
right = Sensor(INPUT_3)

left.mode = "RAW"
right.mode = "RAW"

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)

leftLocked = False
rightLocked = False
while not rightLocked or not leftLocked:

    print("LEFT: " + str(left.value()) + " RIGHT: " + str(right.value()))

    if left.value() > 100 and not leftLocked:
        lm.on(-10)
    else:
        leftLocked = True
        lm.on(2)
    if right.value() > 100 and not rightLocked:
        rm.on(-10)
    else:
        rightLocked = True
        rm.on(2)


leftLocked = False
rightLocked = False
while not rightLocked or not leftLocked:

    print("LEFT: " + str(left.value()) + " RIGHT: " + str(right.value()))

    if left.value() < 200 and not leftLocked:
        lm.on(-5)
    else:
        leftLocked = True
        lm.off()
    if right.value() < 200 and not rightLocked:
        rm.on(-5)
    else:
        rightLocked = True
        rm.off()

rm.off(brake=True)
lm.off(brake=True)


