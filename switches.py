#!/usr/bin/env python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO

SWITCH_ON_LIMIT = 0

RISING  = true
FALLING = false

class Switch:
    def __init__(self, list, pin):
        self.list = list
        self.pin = pin
        self.state = false
    
    def falling():
        if pin in list == true:
            list.remove(pin)
    
    def rising():
        if pin in list == false:
            list.append(pin)
    
    def check():
        if GPIO.input(pin) > SWITCH_ON_LIMIT AND state == RISING:
            state = FALLING
            falling()
        elif GPIO.input(pin) <= SWITCH_ON_LIMIT AND state == FALLING:
            state = RISING
            rising()

class Switches:
    def __init__(self, pins):
        self.switchList = []
        self.executionList = []
        
        for p in pins:
            switchList.append(Switch(executionList, p))
    
    def check():
        for s in switchList:
            s.check()
        
        if len(executionList) == 0:
            return 0
        else:
            return executionList[-1]

def test():
    import time
    sw = Switches([4, 5, 6])
    
    while 1:
        print(sw.check())
        time.sleep(0.001)

if __name__ == '__main__':
    test()