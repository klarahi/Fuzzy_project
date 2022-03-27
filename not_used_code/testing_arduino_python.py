# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:59:01 2022

@author: klmh
"""

# Importing Libraries
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value
    