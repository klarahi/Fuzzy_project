# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:30:25 2022

@author: klmh
"""

import numpy as np


#to fix the path
import os
if not os.path.isabs(path):
    path = os.path.join(os.path.dirname(sys.argv[0]), path)



import cv2


#loading image (empty matrix if problem)
img = cv2.imread(filename)