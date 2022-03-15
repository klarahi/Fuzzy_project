# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:09:30 2022

@author: klmh
"""

""" first program that can controll the laserpointer by input catergory """

'''
NOT USING THIS
#defining box position and name manual
box_1 = [(90, 90, 90), 'Sensor 1']
box_2 = [(100, 90, 90), 'Sensor 2']
box_3 = [(120, 100, 90), 'Motor 1']
box_4 = [(70, 90, 90), '']
box_5 = [(90, 70, 90)]
box_6 = [(85, 110, 90)]
'''
#import sys  #early termination
#import os  #early termination
import serial
import time

def file_to_dictionary(filepath):
    '''
    Function that takes a txt file with part names and coordinates. 
    And splits those in its two parts and puts those into a dictionary, if file is formated as "Name(x,y,r)" with one name per line.

    Parameters
    ----------
    filepath : string
        path to the txt file with the part names and coordinates.

    Returns
    -------
    a dictionary with names as key and coordinates as string in format "x,y,r\n"

    '''
    #reads file with box names and coordinates
    calibrated_boxes = open(filepath)
    #if not os.path.isabs(calibrated_boxes):
    #    calibrated_boxes = os.path.join(os.path.dirname(sys.argv[0]), calibrated_boxes)
    boxes_info = calibrated_boxes.readlines()
    calibrated_boxes.close()
    
    boxes = {}
    
    #Making a dicrectionary out of the read data from file
    for line in boxes_info:
        infos = line.split('(')
        name = infos[0]
        coordinates = infos[1].replace(')', '')
        boxes[name] = coordinates
        #DEBUG: print(name, coordinates)
        
    return boxes
    
def asking_for_part(boxes):
    '''
    Parameters : boxes, TYPE = dictionary, with all box names and cooerdinates
    rints all keys from dictionary, ask you to choose one of them
    
    -------
    coordinates_part : STRING
        Coordinates to wished part. (value of dictonary from whished key)
    '''
    #prits all parts (keys) in an alphabetic sorted list
    print('All parts detected:\n', boxes.keys())
    #takes inn part looked for
    part_desired = input("Write the part you are looking for from the list above: ")
    
    #gets the coordinatestring from the desired part
    #BUG: prints not found even though is is found
    coordinates_part = boxes.get(part_desired)
    return coordinates_part

def coordinates_to_arduino(coordinates):
    #opens the connection to ardoinoen
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    #sends the coordinates to ardoino code in utf-8 encoding
    arduino.write(coordinates.encode("utf-8"))
    #waits for 2 sec
    time.sleep(2)
    #closes port
    arduino.close()
    return

if __name__ == "__main__":
    boxes = file_to_dictionary("C:\\Users\\klmh\\OneDrive\\Dokumente\\NTNU\\TMM4245_Fuzzy_Front_End\\box_coordinates.txt")
    part = asking_for_part(boxes)
    coordinates_to_arduino(part)
    
    



