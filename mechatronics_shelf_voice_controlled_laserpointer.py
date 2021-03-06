# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:09:30 2022

@author: klmh
"""

""" first program that can controll the laserpointer by input catergory """

#import sys  #early termination
#import os  #early termination
import serial
import time
import voice_recognition

def file_to_listing(filepath):
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
    
    boxes = []
    
    #Making a dicrectionary out of the read data from file
    for line in boxes_info:
        infos = line.split('- ')
        if len(infos) < 2:
            None
        else:
            name = infos[1:]
            coordinates = infos[0]+'\n'
            boxes.append((name, coordinates))

    return boxes
    
def showing_parts(boxes):
    '''
    Parameters : boxes, TYPE = dictionary, with all box names and cooerdinates
    rints all keys from dictionary, ask you to choose one of them
    
    -------
    coordinates_part : STRING
        Coordinates to wished part. (value of dictonary from whished key)
    '''
    #prits all parts (keys) in an alphabetic sorted list
    boxes_names = []
    coordinates_part = '63,69,90\n'
    for thing in range(len(boxes)):
        boxes_names.append(boxes[thing][0])
        boxes_names.sort()
    print('All parts detected:')
    for name in boxes_names:
        print(*name)
    #takes inn part looked for
    return

def finding_coordinates(part_desired, boxes):
    #gets the coordinatestring from the desired part
    part_desired = part_desired.lower()
    found = 0
    for thing in range(len(boxes)):
        if boxes[thing][0].lower() == part_desired:
            coordinates_part = boxes[thing][1]
            found = 1
            break
    if found == 0:
        print("part not found")

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
    boxes = file_to_listing("C:\\Users\\klmh\\OneDrive\\Dokumente\\NTNU\\TMM4245_Fuzzy_Front_End\\shelfB.txt")
    showing_parts(boxes)
    #part = input("Write the part you are looking for from the list above: ")
    print("What part are you looking for?")
    part = Speech_to_text()
    part_coordinates = finding_coordinates(part, boxes)
    coordinates_to_arduino(part_coordinates)

    
    



