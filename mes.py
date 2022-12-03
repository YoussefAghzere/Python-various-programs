#!/usr/bin/python3
import time
import pyautogui as pg
count = 0
time.sleep(5)
liste = ['hello', 'youssef']
while True:
    #m1, m2 = pg.position()
    #time.sleep(1)
    #print(str(m1) + "," + str(m2))
    pg.click(1009, 339)
    time.sleep(1)
    pg.write('aghzerey@gmail.com')
    pg.click(983, 465)
    time.sleep(1)
    pg.write(liste[count])
    pg.click(1090, 645)
    time.sleep(5)
    count += 1;
    count %= len(liste)
