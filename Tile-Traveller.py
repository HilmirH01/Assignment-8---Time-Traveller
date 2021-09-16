x = 1
y = 1


#Fastar fyrir strengi
TRAVEL_STR = "You can travel:"
DIRECTION_N = " (N)orth"
DIRECTION_S = " (S)outh"
DIRECTION_E = " (E)ast"
DIRECTION_W = " (W)est"
ERROR_DIR = "Not a valid direction!" #For when the user inputs an impossible direction.
OR_STR = " or"
DOT_STR = "."
GREETING = """You have stumbled upon Darth Vader 
and he desparately needs your help 
figuring out the correct way through
the maze. Darth Vader: 'Help me, or else'..."""

#Breytur sem inniheldur strengina með áttunum.
tile_1_1_dir = (TRAVEL_STR + DIRECTION_N + DOT_STR)
tile_1_2_dir = (TRAVEL_STR + DIRECTION_N + OR_STR + DIRECTION_E + OR_STR + DIRECTION_S + DOT_STR)
tile_1_3_dir = (TRAVEL_STR + DIRECTION_E + OR_STR + DIRECTION_S + DOT_STR)
tile_2_1_dir = (TRAVEL_STR + DIRECTION_N + DOT_STR)
tile_2_2_dir = (TRAVEL_STR + DIRECTION_S + OR_STR + DIRECTION_W + DOT_STR)
tile_2_3_dir = (TRAVEL_STR + DIRECTION_E + OR_STR + DIRECTION_W + DOT_STR)
tile_3_3_dir = (TRAVEL_STR + DIRECTION_S + OR_STR + DIRECTION_W + DOT_STR)
tile_3_2_dir = (TRAVEL_STR + DIRECTION_N + OR_STR + DIRECTION_S + DOT_STR)
winning_tile_3_1 = "Victory!"

tile_maze_start = ''' 
 __________________________________________________
|                |                |                |
|                |                |                |
|                |                |                |
|                                                  |
|                |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                                 |                |
|                |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|      /"\       |                |                |
|     /*_*\ /    |                |     WORLD      |
|      (|--/     |                |  DESTRUCTION   |
|     _/ \_      |                |                |
|                |                |                |
|________________|________________|________________|
'''

tile_maze_1_2 = ''' 
 __________________________________________________
|                |                |                |
|                |                |                |
|                |                |                |
|                                                  |
|                |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|      /"\       |                |                |
|     /*_*\ /    |                |                |
|      (|--/                      |                |
|     _/ \_      |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|________________|________________|________________|
'''

tile_maze_1_3 = ''' 
 __________________________________________________
|                |                |                |
|      /"\       |                |                |
|     /*_*\ /    |                |                |
|      (|--/                                       |
|     _/ \_      |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                                 |                |
|                |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|________________|________________|________________|
'''

tile_maze_2_1 = ''' 
 __________________________________________________
|                |                |                |
|                |                |                |
|                |                |                |
|                                                  |
|                |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                                 |                |
|                |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |      /"\       |                |
|                |     /*_*\ /    |                |
|                       (|--/     |                |
|                |     _/ \_      |                |
|                |                |                |
|________________|________________|________________|
'''
tile_maze_2_2 = ''' 
 __________________________________________________
|                |                |                |
|                |                |                |
|                |                |                |
|                                                  |
|                |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |      /"\       |                |
|                |     /*_*\ /    |                |
|                       (|--/     |                |
|                |     _/ \_      |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|________________|________________|________________|
'''

tile_maze_2_3 = ''' 
 __________________________________________________
|                |                |                |
|                |      /"\       |                |
|                |     /*_*\ /    |                |
|                       (|--/                      |
|                |     _/ \_      |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                                 |                |
|                |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|________________|________________|________________|
''' 

tile_maze_3_3 = ''' 
 __________________________________________________
|                |                |                |
|                |                |      /"\       |
|                |                |     /*_*\ /    |
|                                        (|--/     |
|                |                |     _/ \_      |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                                 |                |
|                |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|________________|________________|________________|
'''

tile_maze_3_2 = ''' 
 __________________________________________________
|                |                |                |
|                |                |                |
|                |                |                |
|                                                  |
|                |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |      /"\       |
|                |                |     /*_*\ /    |
|                                 |      (|--/     |
|                |                |     _/ \_      |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|________________|________________|________________|
'''

tile_maze_3_1 = ''' 
 __________________________________________________
|                |                |                |
|                |                |                |
|                |                |                |
|                                                  |
|                |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                                 |                |
|                |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |      /"\       |
|                |                |     /*_*\ /    |
|                                        (|--/     |
|                |                |     _/ \_      |    
|                |                |    VICTORY!    |
|________________|________________|________________|
'''

tile_maze_empty = ''' 
 __________________________________________________
|                |                |                |
|                |                |                |
|                |                |                |
|                                                  |
|                |                |                |
|                |                |                |
|______    ______|________________|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                                 |                |
|                |                |                |
|                |                |                |
|______    ______|______    ______|______    ______|
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|                |                |                |
|________________|________________|________________|
'''


player_sketch = '''
        
      /"\ 
     /*_*\ /
      (|--/
     _/ \_ 
'''

print()
print()
print(GREETING)


while x != 3 or y != 1:
    #Starting tile 1,1    
    if x == 1 and y == 1:
        print(tile_maze_start)
        print(tile_1_1_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        else:
            print(ERROR_DIR)
        

#When entering tile 1,2    
    elif x == 1 and y == 2:
        print(tile_maze_1_2)
        print(tile_1_2_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        elif dir_input == "e" or dir_input == "E":
            x += 1 
        elif dir_input == "s" or dir_input == "S":
            y -= 1
        else:
            print(ERROR_DIR)

#When entering tile 1,3
    elif x == 1 and y == 3:
        print(tile_maze_1_3)
        print(tile_1_3_dir)
        dir_input = input("Direction: ")
        if dir_input == "s" or dir_input == "S":
            y -= 1
        elif dir_input == "e" or dir_input == "E":
            x += 1
        else:
            print(ERROR_DIR)

#When entering tile 2,1
    elif x == 2 and y == 1:
        print(tile_maze_2_1)
        print(tile_2_1_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        else:
            print(ERROR_DIR)

#When entering tile 2,2
    elif x == 2 and y == 2:
        print(tile_maze_2_2)
        print(tile_2_2_dir)
        dir_input = input("Direction: ")
        if dir_input == "s" or dir_input == "S":
            y -= 1
        elif dir_input == "w" or dir_input == "W":
            x -= 1
        else:
            print(ERROR_DIR)

#When entering tile 2,3
    elif x == 2 and y == 3:
        print(tile_maze_2_3)
        print(tile_2_3_dir)
        dir_input = input("Direction: ")
        if dir_input == "w" or dir_input == "W":
            x -= 1
        elif dir_input == "e" or dir_input == "E":
            x += 1
        else:
            print(ERROR_DIR)

#When entering tile 3,3
    elif x == 3 and y == 3:
        print(tile_maze_3_3)
        print(tile_3_3_dir)
        dir_input = input("Direction: ")
        if dir_input == "w" or dir_input == "W":
            x -= 1
        elif dir_input == "s" or dir_input == "S":
            y -= 1
        else:
            print(ERROR_DIR)

#When entering tile 3,2
    elif x == 3 and y == 2:
        print(tile_maze_3_2)
        print(tile_3_2_dir)
        dir_input = input("Direction: ")
        if dir_input == "n" or dir_input == "N":
            y += 1
        elif dir_input == "s" or dir_input == "S":
            y -= 1
        else:
            print(ERROR_DIR)

#When entering tile 3,1
    if x == 3 and y == 1:
        print(tile_maze_3_1)
        print(winning_tile_3_1) #Prints out the winning message, and goes to the top of the while loop and ends because the condition is no longer met.
        print("""Darth Vader thanks you for the help, 
he will forever be in your debt.""")    






#def tile_1_1(direction):
    #x = 1 
    #y = 1
    #print(tile_1_1_dir + ".")
    #direction = input("Direction: ")
    #if direction == "n" or direction == "N":
        #y += 1
        #x += 0
    #else:
        #print(ERROR_DIR)
    #return direction

#print(tile_1_1("n"))

    