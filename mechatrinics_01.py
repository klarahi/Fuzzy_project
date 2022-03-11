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

def name_to_coordinates(filepath):
    '''
    Program that takes a txt file with part names and coordinates. 
    Asks you what part you want and returns its coordinates.

    Parameters
    ----------
    filepath : string
        path to the txt file with the part names and coordinates.

    Returns
    -------
    coordinates to chosen part.

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
        #DEBUG print(name, coordinates)
    
    '''
    #defining box position and name manual as dictionary
    # string with name of box and sting with coordinates (a string in the form: x,y,r\n where '\n' is the newline character) for laser
    boxes = {"Sensor 1":"70,70,90\n",
             "Sensor 2":"70,80,90\n",
             "Sensor 3":"70,90,90\n",
             "Motor 1":"80,70,90\n",
             "Motor 2":"80,80,90\n",
             "Camera":"80,90,90\n",
             "Microphone":"90,80,90\n"}
    '''
    
    print('All parts detected:\n', boxes.keys())
    
    part_desired = input("Write the part you are looking for: ")
    
    #gets the coordinatestring from the desired part
    #BUG: prints not found even though is is found
    coordinates_part = boxes.get(part_desired)
    return coordinates_part

if __name__ == "__main__":
    coordinates = name_to_coordinates("C:\\Users\\klmh\\OneDrive\\Dokumente\\NTNU\\TMM4245_Fuzzy_Front_End\\box_coordinates.txt")
    print(coordinates)

