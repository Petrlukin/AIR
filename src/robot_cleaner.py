#!/usr/bin/env python

import numpy as np

#read from the file
def two_d_map_array(map):
        number_of_lines = 0
        map_array = np.array([[]])
        for line in map:
            signs_in_line = 0
            number_of_lines = number_of_lines + 1
            for sign in line:
                if sign == ' ': #empty
                    map_array = np.append(map_array, 0)
                    signs_in_line = signs_in_line + 1
                elif sign == '\n': #change of the line
                    pass
                elif sign == '*': #dirt
                    map_array = np.append(map_array, 2)
                    signs_in_line = signs_in_line + 1
                elif sign == 's':#robot
                    map_array = np.append(map_array, 3)
                elif sign == '-': #searched
                    map_array = np.append(map_array, 1)
                else: #obstacles
                    map_array = np.append(map_array, 4)
                    signs_in_line = signs_in_line + 1 
        map_array = np.reshape(map_array, (number_of_lines, signs_in_line))
        return map_array

#find robot


if __name__ == "__main__":
    #read from the file
    map_array = np.array([[]])  
    
    map_number = input("Please, input the number of a map (1-3).")
    if map_number == 1:
        map = open('map1.txt')
        map_array = two_d_map_array(map)
    elif map_number == 2:
        map = open('map2.txt')
        map_array = two_d_map_array(map)
    else: # if anything but "3" was inputed, anyway call the third map
        map = open('map3.txt')
        map_array = two_d_map_array(map)
    print map_array
        
        
		
