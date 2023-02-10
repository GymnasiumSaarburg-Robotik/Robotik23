#!/usr/bin/env python3

from ev3dev2.sensor import Sensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C
from ev3dev2.motor import LargeMotor


def align_backwards():
    left = Sensor(INPUT_2)
    right = Sensor(INPUT_3)
    left.mode = "RAW"
    right.mode = "RAW"
    lm = LargeMotor(OUTPUT_B)
    rm = LargeMotor(OUTPUT_C)
    leftLocked = False
    rightLocked = False
    while not rightLocked or not leftLocked:

        if left.value() > 100 and not leftLocked:
            if rightLocked:
                lm.on(-10)
            else:
                lm.on(-20)
        else:
            leftLocked = True
            lm.on(-3)
        if right.value() > 100 and not rightLocked:
            if leftLocked:
                rm.on(-10)
            else:
                rm.on(-20)
        else:
            rightLocked = True
            rm.on(-3)
    leftLocked = False
    rightLocked = False
    while not rightLocked or not leftLocked:
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


def align_forwards():
    left = Sensor(INPUT_2)
    right = Sensor(INPUT_3)
    left.mode = "RAW"
    right.mode = "RAW"
    lm = LargeMotor(OUTPUT_B)
    rm = LargeMotor(OUTPUT_C)
    leftLocked = False
    rightLocked = False
    while not rightLocked or not leftLocked:

        if left.value() > 100 and not leftLocked:
            if rightLocked:
                lm.on(10)
            else:
                lm.on(20)
        else:
            leftLocked = True
            lm.on(3)
        if right.value() > 100 and not rightLocked:
            if leftLocked:
                rm.on(10)
            else:
                rm.on(20)
        else:
            rightLocked = True
            rm.on(3)
    leftLocked = False
    rightLocked = False
    while not rightLocked or not leftLocked:
        if left.value() < 200 and not leftLocked:
            lm.on(5)
        else:
            leftLocked = True
            lm.off()
        if right.value() < 200 and not rightLocked:
            rm.on(5)
        else:
            rightLocked = True
            rm.off()
    rm.off(brake=True)
    lm.off(brake=True)
