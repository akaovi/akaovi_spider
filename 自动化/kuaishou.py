# coding: utf-8
#
import uiautomator2 as u2
import time
import random

d = u2.connect()

d(text="快手极速版").click()
time.sleep(3)
while True:
    d.swipe(0.6, 0.7, 0.9, 0.001)
    time.sleep(random.randint(5, 7))
