# _*_ coding: utf-8 _*_
# @Time     : 2019/10/8 0:56
# @Author   : Ole211
# @Site     : 
# @File     : display_time.py    
# @Software : PyCharm

import smbus
import time
import sys
import LCD1602 as LCD
import logx
import logging

if __name__ == '__main__':
    LCD.init_lcd()
    time.sleep(2)
    LCD.print_lcd(0,0,'NUPT bear BLight')
    LCD.print_lcd(1,1,'local time')
    logging.info('wait 2 seconds')
    LCD.turn_light(1)
    logging.info('turn on BLight')
    time.sleep(5)
    while True:
        nowtime = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
        hourtime = time.strftime('%H',time.localtime(time.time()))
        mintime = time.strftime('%M',time.localtime(time.time()))
        sectime = time.strftime('%S',time.localtime(time.time()))
        LCD.print_lcd(1,1,nowtime)
        if mintime == '59':
            if sectime == '00':
                LCD.turn_light(1)
            elif sectime  == '59':
                LCD.turn_light(0)
        time.sleep(1)