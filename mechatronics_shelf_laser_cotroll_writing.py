# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:09:30 2022

@author: klmh

first program that can controll the laserpointer by input catergory
"""

# import sys  #early termination
# import os  #early termination
import serial
import time

def file_to_listing(filepath: str) -> list:
    '''
    Function that takes a txt file with part names and coordinates.
    And splits those in its two parts and puts those into a dictionary, if file is formated as "Name(x,y,r)" with one name per line.

    Parameters
    ----------
    filepath : string
        path to the txt file with the part names and coordinates.

    Returns
    -------
    a list with tupels where names are on first and coordinates as string in format "x,y,r\n" on second position.

    '''
    # reads file with box names and coordinates
    calibrated_boxes = open(filepath)
    # if not os.path.isabs(calibrated_boxes):
    #    calibrated_boxes = os.path.join(os.path.dirname(sys.argv[0]), calibrated_boxes)
    boxes_info = calibrated_boxes.readlines()
    calibrated_boxes.close()

    #creating empty list for all boxes
    boxes = []

    # Making the list out of the read data from file
    # reads out name and coordinates if formated "coordinate - name" per line
    for line in boxes_info:
        infos = line.split('- ')
        #if just one "word" nothing is done
        if len(infos) < 2:
            pass
        else:
            name = infos[1].replace('\n', '')
            coordinates = infos[0] + '\n'
            boxes.append((name, coordinates))

    return boxes


def asking_for_part(boxes: list) -> str:
    '''
    Parameters : boxes, TYPE = list with tuples, with all box names and coordinates :(name, coordinate)
    prints all names from list, ask you to choose one of them

    Returns
    -------
    coordinates_part : STRING
        Coordinates to wished part.
    '''
    #prits all parts in an alphabetic sorted list
    #boxes_names = [thing[0] for thing in boxes]
    coordinates_part = '63,69,90\n'
    boxes_names = []
    index = 0
    for thing in boxes:
        #boxes_names.append(boxes[int(boxes.index(thing))][0])
        boxes_names.append(boxes[index][0])
        index += 1
    boxes_names.sort()

    print('All parts detected:\n')
    #print(boxes_names)
    for name in boxes_names:
        print(name)

    # takes inn part looked for
    part_desired = input("\nWrite the part you are looking for from the list above: ")

    # gets the coordinatestring from the desired part
    part_desired = part_desired.lower()
    found = 0
    for thing in boxes:
        index = int(boxes.index(thing))
        part = boxes[index][0]
        if part == part_desired:
            coordinates_part = boxes[index][1]
            found = 1
            break
    if found == 0:
        print("part not found")

    return coordinates_part


def coordinates_to_arduino(coordinates: str) -> None:
    # opens the connection to ardoinoen
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    # sends the coordinates to ardoino code in utf-8 encoding
    arduino.write(coordinates.encode("utf-8"))
    # waits for 2 sec
    time.sleep(10)
    # closes port
    arduino.close()
    return


if __name__ == "__main__":
    boxes = file_to_listing("shelfB.txt")
    #print(boxes)
    part = asking_for_part(boxes)
    print(part)
    part_utf8 = part.encode("utf-8")
    print(part_utf8)
    coordinates_to_arduino(part)




