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
def find_robot(map_array):
    robot_position = np.where(map_array == 3)
    return robot_position

#find dirt
def find_all_dirt(map_array):
    dirt_position = np.where(map_array == 2)
    dirt_position = np.append([], dirt_position)
    
    return len(dirt_position)/2

#Depth-First Search
 
def children(map_array, position, dirt_number):
    #print map_array
    if (map_array[position[0]-1][ position[1]] != 4) and (map_array[position[0]-1][ position[1]] != 1):
        left_child = np.array([position[0]-1, position[1]])
    else:
        left_child = []
    
    if (map_array[position[0]][ position[1]+1] != 4) and (map_array[position[0]][ position[1]+1] != 1):
        up_child = np.array([position[0], position[1]+1])        
    else:
        up_child = []

    if (map_array[position[0]+1][ position[1]] != 4) and (map_array[position[0]+1][ position[1]] != 1):
        right_child  = np.array([position[0]+1, position[1]])
        #print right_child
    else:
        right_child  = []

    if( map_array[position[0]][ position[1]-1] != 4) and (map_array[position[0]][ position[1]-1] != 1):
        down_child = np.array([position[0], position[1]-1])
    else:
        down_child = []

    if map_array[position[0]][ position[1]] == 2:
        print "Position of a dirt pile"
        print position[0], position[1]
        dirt_number = dirt_number + 1
    map_array[position[0]][ position[1]] = 1
    
    return left_child, up_child, right_child, down_child, dirt_number, map_array

def go_tree(left_child, up_child, right_child, down_child, stack):
    if left_child != []:
        stack = np.row_stack((left_child, stack))
    if up_child != []:
        stack = np.row_stack((up_child, stack))
    if right_child != []:
        stack = np.row_stack((right_child, stack))
    if down_child != []:
        stack = np.row_stack((down_child, stack))
    #print "***"
    #print stack
    #print "***"
    return stack
   

if __name__ == "__main__":
    #read from the file
    map_array = np.array([[]])  
    left_child = np.array([[]])
    up_child = np.array([[]])
    right_child = np.array([[]])
    down_child = np.array([[]])
    dirt_number = 0
    
    
    map_number = input("Please, input the number of a map (1-3).")
    if map_number == 1:
        map = open('map1.txt')
        map_array = two_d_map_array(map)
    elif map_number == 2:
        map = open('map2.txt')
        map_array = two_d_map_array(map)
    elif map_number == 3:
        map = open('map3.txt')
        map_array = two_d_map_array(map)
    else: # if anything but "3" was inputed, anyway call the third map
        map = open('map4.txt')
        map_array = two_d_map_array(map)

    #find robot 
    robot_position = np.append([], find_robot(map_array))
     
    start = np.array([robot_position[0], robot_position[1]])
  
    #find dirt    
    fin_number_of_dirt = find_all_dirt(map_array)
    #print fin_number_of_dirt

    #Depth-First Search    
   
    
    stack = start

    
    position = start
    #print "Stack:\n"
    #print stack
    #print "Position:\n"
    #print position
    #print "-----------"
    #Depth-First Search 
    while(len(stack) != 0):
    #for i in map_array:
    #    for j in i:
        #print "position"
        #print position
        chlds = children(map_array, position, dirt_number)
        dirt_number = chlds[4]
        map_array = chlds[5]
        #print "Children:"
        #print "---------"
        #print chlds[0], chlds[1], chlds[2], chlds[3]
        #print "---------"
        stack = go_tree(chlds[0], chlds[1], chlds[2], chlds[3], stack)
        #print len(stack)
        #raw_input("Press Enter to continue...")
        #print stack
        
        position = stack[0]
        #print len(stack)            
        stack = np.delete(stack, 0, 0)
    print "Number of dirt piles"
    print dirt_number